<?php 
 include('Food_Ordering_System\partials-front\menu.php'); ?>
 <?php
$sql = "SELECT AVG(pizza) as pizza_avg FROM neworder";
$sql1 = "SELECT AVG(Burger) as burger_avg FROM neworder";
$sql2 = "SELECT AVG(Noodle) as noodle_avg FROM neworder";

// Performing queries
$pizza_result = mysqli_query($conn, $sql);
$burger_result = mysqli_query($conn, $sql1);
$noodle_result = mysqli_query($conn, $sql2);

// Checking if the queries returned results
if(mysqli_num_rows($pizza_result) > 0 && mysqli_num_rows($burger_result) > 0 && mysqli_num_rows($noodle_result) > 0) {
    // Fetching the average values
    $pizza_avg = mysqli_fetch_assoc($pizza_result)['pizza_avg'];
    $burger_avg = mysqli_fetch_assoc($burger_result)['burger_avg'];
    $noodle_avg = mysqli_fetch_assoc($noodle_result)['noodle_avg'];

    // Outputting the results
    echo "Pizza : " . (int)$pizza_avg . "<br>";
    echo "Burger : " . (int)$burger_avg . "<br>";
    echo "Noodle : " . (int)$noodle_avg . "<br>";
} else {
    // If no results were returned
    echo "No data found";
}
?>
