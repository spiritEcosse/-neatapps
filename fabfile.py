__author__ = 'igor'

from fabric.api import local, run, require, cd, settings
import os
from neatapps.settings import BASE_DIR
from fabric.state import env
# env.hosts = ['root@78.24.216.187', 'root@185.65.247.131']
env.user = 'root'
env.skip_bad_hosts = True
env.warn_only = True
env.parallel = True
HOSTS = [('root@78.24.216.187', '/home/igor/web/www/neatapps'),
         ('root@185.65.247.131', '/home/neatapps/web/www/neatapps')]
REQUIREMENTS_FILE = 'requirements.txt'
TORNADO_SCRIPT = 'tornado_main.py'


def deploy():
    """
    deploy project on remote server
    :return:
    """
    local_act()
    update_requirements()
    remote_act()


def remote_act():
    """
    run remote acts
    :return: None
    """
    for host, dir_name in HOSTS:
        with settings(host_string=host):
            with cd(dir_name):
                run("git reset --hard")
                run("kill $(ps aux | grep 'python %s/tornado_main.py')" % BASE_DIR, capture=True)
                run("python %s/tornado_main.py > /dev/null 2>&1 &" % BASE_DIR)


def local_act():
    """
    prepare deploy
    :return: None
    """
    os.environ.setdefault("DJANGO_SETTINGS_MODULE", "neatapps.settings")
    activate_env = os.path.expanduser(os.path.join(BASE_DIR, ".env/bin/activate_this.py"))
    execfile(activate_env, dict(__file__=activate_env))
    local("./manage.py test")
    local("./manage.py compilemessages")
    local("%s%s" % ('pip freeze > ', REQUIREMENTS_FILE))
    local("./manage.py collectstatic -c --noinput")
    local("git add .")
    local("git commit -a -F git_commit_message")
    current_branch = local("git symbolic-ref --short -q HEAD", capture=True)

    if current_branch != 'master':
        local("git checkout master")
        local("git merge %s" % current_branch)
        local("git branch -d %s" % current_branch)

    local("git push origin")
    local("git push production")
    local("git push my_repo_neatapps_bit")
    local("git push my-production")


def update_requirements():
    """
    install external requirements on remote host
    :return: None
    """
    for host, dir_name in HOSTS:
        with settings(host_string=host):
            with cd(dir_name):
                run('%s && %s%s' % ('source .env/bin/activate', 'pip install -r ', REQUIREMENTS_FILE))
