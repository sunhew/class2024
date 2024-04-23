<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Document</title>
</head>

<body>

<?php
    include "connect.php";

    $sql = "SELECT * FROM test";
    $result = $connect -> query($sql);

    if($result){
        $count = $result -> num_rows;

        for($i=0; $i<$count; $i++){
            $info = $result -> fetch_array(MYSQLI_ASSOC);

            // echo "<pre>";
            // var_dump($info);
            // echo "</pre>"

            echo "<ul>";
            echo "<ll> 이름 : ". $info['testName'] ."</ll>";
            echo "<ll> 인사말 : ".$info['testText'] ."</ll>";
            echo "<ll> 기록 : ".$info['regTime'] ."</ll>";
            echo "</ul>";
        }
    }
?>

</body>

</html>