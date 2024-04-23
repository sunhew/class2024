<?php
    include "../connect/connect.php";

    $sql = "CREATE TABLE test(";
    $sql .= "testID int(10) unsigned auto_increment,";
    $sql .= "testName varchar(10) NOT NULL,";
    $sql .= "testText varchar(100) NOT NULL,";
    $sql .= "regTime int(30) NOT NULL,";
    $sql .= "PRIMARY KEY(memberID)";
    $sql .= ") charset=utf8;";

    $result = $connect -> query($sql);

    if($result){
        echo "Create Tables True";
    }else{
        echo "Create Tables false";
    }
?>