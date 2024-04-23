<?php
    $host = "localhost";
    $user = "gsim12";
    $pw = "chltjsghk1932#";
    $db = "gsim12";

    $connect = new mysqli($host, $user, $pw, $db);
    $connect -> set_charset("utf-8");

    if(mysqli_connect_errno()){
        echo "DATABASE Connect False";
    } else {
        echo "DATABASE Connect True";
    }
?>