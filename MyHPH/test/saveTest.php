<?php
    include "connect.php";

    $testName = "최선화";
    $testText = "안녕하세요";
    $regTime = time();

    // echo $testName, $testText, $regTime;

    // 데이터 넣기
    $sql = "INSERT INTO test(testName, testText, regTime) VALUES('testName', 'testText', 'regTime')";
    $connect -> query($sql);
?>