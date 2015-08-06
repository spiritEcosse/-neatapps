<?php
    $name = $_POST['name'];
    $email = $_POST['email'];
    $message = $_POST['message'];

    $to = 'info@neatapps.co';
    $subject = 'the subject';
    $message = 'FROM: '.$name.' Email: '.$email.'Message: '.$message;
    $headers = 'From: youremail@domain.com' . "\r\n";

    if (filter_var($email, FILTER_VALIDATE_EMAIL)) {
        mail($to, $subject, $message, $headers);
        echo "Email was sent!";
    } else {
        echo "Invalid Email.";
    }
?>