<?php
$servername= "localhost";
$username="root";
$password= "";
$dbname= "carbonfootprint";


echo "done";
$electricity=$_POST['electricity'];
$petrol=$_POST['petrol'];
$diesel=$_POST['diesel'];
$cook=$_POST['cook'];
$fuel=$_POST['fuel'];
$conn = new mysqli($servername, $username, $password, $dbname);

if($conn->connect_error){
    die("Connection failed : " . $conn->connect_error);
}
echo "Connected Successfully";


$ce= ($electricity*1.1845) + ($petrol * 2.983) + ( $diesel* 2.653)+ ( $cook* $fuel);
$q1="INSERT INTO `carbon`(`power`, `petrol`, `diesel`, `lpg`, `cemission`) VALUES ('$electricity','$petrol','$diesel','$cook','$ce')";
echo $ce;
if($conn->query($q1) === TRUE){
    echo "New record created successfully";
}else{
    echo " Error: " . $q1 . "<br>" . $conn->error;
}
echo "Carbon emission : " . $petrol;
$conn->close();
header("Location: form_3.html");
?>