<?php
// establish a connection to the database
$conn = mysqli_connect("localhost:3307", "root", "", "cinema_db");

// check if the connection was successful
if (!$conn) {
    die("Connection failed: " . mysqli_connect_error());
}

// select the sum of the bookingType column from the bookingtable
$movieQuery = "SELECT SUM(bookingType) AS sum FROM bookingtable";
$result = mysqli_query($conn, $movieQuery);

// check if the query was successful
if (!$result) {
    die("Error executing query: " . mysqli_error($conn));
}

// fetch the sum of the bookingType column from the result
$row = mysqli_fetch_array($result);
$bookedSeats = $row['sum'];

// calculate the number of available seats
$totalSeats = 36;
$availableSeats = $totalSeats - $bookedSeats;
if($availableSeats>=0)
{
// output the number of available seats
echo $availableSeats . ' Seats Available';
}
else
{
    echo ' 0 Seats Available';
}
// close the database connection
mysqli_close($conn);
?>
