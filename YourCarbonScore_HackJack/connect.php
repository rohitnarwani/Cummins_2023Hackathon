<?php
$servername= "localhost";
$username="root";
$password= "";
$dbname= "carbonfootprint";

/*
$power=$_POST[''];
$petrol=$_POST[''];
$lpg=$_POST[''];

$species=$_POST[''];
$height=$_POST[''];
$season=$_POST[''];
$place=$_POST[''];
$location=$_POST[''];
*/

$name=$_POST['name'];
$phone=$_POST['phone'];
$street=$_POST['street'];
$country=$_POST['country'];
$zipcode=$_POST['zip'];
$gender=$_POST['gender'];
$state=$_POST['state'];
$city=$_POST['city'];




$conn = new mysqli($servername, $username, $password, $dbname);

if($conn->connect_error){
    die("Connection failed : " . $conn->connect_error);
}
echo "Connected Successfully";


$q0="INSERT INTO `member`(`name`, `phone`, `street`, `country`, `zipcode`, `gender`, `state`, `city`) VALUES ('$name','$phone','$street','$country','$zipcode','$gender','$state','$city')";
if($conn->query($q0) === TRUE){
    echo "New record created successfully";
}else{
    echo " Error: " . $sql . "<br>" . $conn->error;
}




header("Location: form2.html");
echo "done";
$vehicles=$_POST['vehicles'];
$petrol=$_POST['petrol'];
$diesel=$_POST['diesel'];

$ce= ($power*4.9102) + ($petrol * 2.453) + ($lpg * 2.903);
$q1="INSERT INTO `carbon`(`id`, `power`, `petrol`, `diesel`, `lpg`, `cemission`) VALUES) VALUES ('[value-1]','50.6','$petrol','$diesel','1.2','2.5','$ce')";
echo $ce;
if($conn->query($q1) === TRUE){
    echo "New record created successfully";
}else{
    echo " Error: " . $sql . "<br>" . $conn->error;
}
/*
$carbon= ($power*0.85) + ($petrol * 2.453) + ($lpg * 2.903);

$q1="INSERT INTO `carbon`( `power`, `petrol`, `lpg`, `cemission`) VALUES ('$power','$petrol','$lpg','$carbon')";

$oxy= $height+ $season/( $place * $location );
$sql = "INSERT INTO `plant`(`species`, `height`, `season`, `place`, `location`, `oxylevel`) VALUES ('$species','$height','$season','$place','$location','$oxy')";
if($conn->query($sql) === TRUE){
    echo "New record created successfully";
}else{
    echo " Error: " . $sql . "<br>" . $conn->error;
}
$cp = $carbon - $oxy;
echo "Carbon emission : " . $carbon . "<br>" . "Oxygen emission : " . $oxy . "<br>" . "Carbon footprint: " . $cp; */
echo "Carbon emission : " . $petrol;
$conn->close();
?>