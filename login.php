<?php
session_start();

if ($_SERVER['REQUEST_METHOD'] == 'POST') {
    $username = $_POST['username'];
    $password = $_POST['password'];

    // Beispiel: Nutzername und Passwort
    $valid_username = "admin";
    $valid_password = "password123";

    if ($username === $valid_username && $password === $valid_password) {
        $_SESSION['loggedin'] = true;
        header('Location: dashboard.php');
        exit;
    } else {
        echo "Ungültiger Benutzername oder Passwort.";
    }
}
?>
