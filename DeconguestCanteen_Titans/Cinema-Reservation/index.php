<!DOCTYPE html>
<html lang="en">

<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <meta http-equiv="X-UA-Compatible" content="ie=edge">
    <link rel="stylesheet" href="style/styles.css">
    <link rel="stylesheet" href="https://use.fontawesome.com/releases/v5.7.2/css/all.css"
        integrity="sha384-fnmOCqbTlWIlj8LyTjo7mOUStjsKC4pOpQbqyi7RrhN7udi9RwhKkMHpvLbHG9Sr" crossorigin="anonymous">
    <!-- <title>BUE Cinema</title> -->
    <!-- <link rel="icon" type="image/png" href="img/logo.png"> -->
</head>
<style>
  /* Styles for the container that holds the cards */
.movies-container {
  display: grid;
  grid-template-columns: repeat(3, 1fr);
  grid-template-rows: repeat(2, auto);
  grid-gap: 20px;
}

/* Default styles for the cards */
.movie-box {
  display: flex;
  flex-direction: column;
  justify-content: center;
  align-items: center;
  text-align: center;
  padding: 10px;
  background-color: #fff;
  box-shadow: 0px 0px 5px rgba(0, 0, 0, 0.1);
}

/* Styles for the movie image */
.movie-box img {
  max-width: 100%;
  height: auto;
  margin-bottom: 10px;
}

/* Styles for the movie title */
.movie-box h3 {
  margin: 0;
  font-size: 1.2rem;
  font-weight: bold;
  text-transform: uppercase;
  color: #f0e9e9;
}

/* Styles for the book a seat link */
.movie-box a {
  display: inline-block;
  margin-top: 10px;
  padding: 10px 20px;
  background-color: #007bff;
  color: #fff;
  text-decoration: none;
  border-radius: 5px;
}

* {
    margin: 0;
    padding: 0;
    box-sizing: border-box;
    font-family: 'Lato', sans-serif;
    text-decoration: none;
    color: white;
}
</style>

<body>
    <?php
    $link = mysqli_connect("localhost:3307", "root", "", "cinema_db");
    $sql = "SELECT * FROM movieTable";
    ?>
    <!-- <header></header> -->
    <div id="home-section-1" class="movie-show-container">
        <!-- <h1>Currently Showing</h1> -->
        <h1><a href="Food_Ordering_System\foods.php">Book a Table now</a> </h1>

        



        <div class="movies-container">
        <?php
    // Retrieve movie data from the database
    $sql = "SELECT movieID, movieTitle, movieImg, numTickets, SUM(bookingtable.bookingType) AS numBookedSeats
            FROM movietable
            LEFT JOIN bookingtable ON movietable.movieTitle = bookingtable.movieName
            GROUP BY movietable.movieID";

    if($result = mysqli_query($link, $sql)){
        if(mysqli_num_rows($result) > 0){
            while($row = mysqli_fetch_array($result)){
                // Calculate the number of available seats
                $available_seats = $row['numTickets'] - $row['numBookedSeats'];

                // Display the movie information and seat availability
                echo '<div class="movie-box">';
                echo '<img src="'. $row['movieImg'] .'" alt=" ">';
                echo '<div class="movie-info ">';
                echo '<h3>'. $row['movieTitle'] .'</h3>';
                echo '<h2>'. $available_seats .' seats available</h2>';
                echo '<a href="booking.php?id='.$row['movieID'].'"><i class="fas fa-ticket-alt"></i> Book a seat</a>';
                echo '</div>';
                echo '</div>';
            }
            mysqli_free_result($result);
        } else{
            echo '<h4 class="no-annot">No Booking to our movies right now</h4>';
        }
    } else{
        echo "ERROR: Could not able to execute $sql. " . mysqli_error($link);
    }
    
    // Close connection
    mysqli_close($link);
?>

        </div>
    </div>
    

    <script src="scripts/jquery-3.3.1.min.js "></script>
    <script src="scripts/script.js "></script>
</body>

</html>