<?php
$servername= "localhost";
$username="root";
$password= "";
$dbname= "carbonfootprint";


echo "done";
$city=$_POST['city'];
$species=$_POST['species'];
$sunlight=$_POST['sunlight'];
$height=$_POST['height'];


$min  = $_POST['data.min'];
$max = $_POST['data.max'];
$conn = new mysqli($servername, $username, $password, $dbname);
$submit = $_POST['submit'];
$quantity=$_POST['quantity'];
$weather=($min+$max)/2;

$humidity=0.02;
$chlorophyll=0.3;
$temperature=23.29;
$oxy=(($height*$sunlight*$chlorophyll)/($temperature*$humidity))/10;
if($conn->connect_error){
    die("Connection failed : " . $conn->connect_error);
}
echo "Connected Successfully";
$oxo= $oxy/100;

$q1="INSERT INTO `planthealth`(`city`, `species`, `sunlight`, `height`, `quantity`, `chlorophyll`, `humidity`, `mintemp`, `maxtemp`, `oxylevel`) VALUES ('$city','$species','$sunlight','$height','$quantity','$chlorophyll','$humidity','$min','$max','$oxy')";

if($conn->query($q1) === TRUE){
    echo "New record created successfully";
}else{
    echo " Error: " . $q1 . "<br>" . $conn->error;
}
echo "Oxygen emission : " . $oxy;
$conn->close();

    header("Location: report.html");

?>
