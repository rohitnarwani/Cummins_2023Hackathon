<?php

session_start();

if(!isset($_SESSION['loggedin']) || $_SESSION['loggedin'] !==true)
{
    header("location: login.php");
}

$uid1 = strtoupper(substr($_SESSION['username'], 0, 1));
$uid2 = $_SESSION['id'] + 9732;
// $uid3 = strtoupper(substr($_SESSION['college'], 0, 2));
// $finaluid = $uid1.$uid2.$uid3;
$finaluid = $uid1.$uid2;

$validationtext = "Authentic Ticket For ".$_SESSION['username']." ID number ".$_SESSION['id']
					?>


<!doctype html>
<html lang="en">

<head>
    <!-- Required meta tags -->
    <meta charset="utf-8">
    <meta name="viewport" content="width=device-width, initial-scale=1, shrink-to-fit=no">
    <!-- for title bar  -->
    <link rel="icon" type="/favicon.ico" href="../images/tickett.png">
    <!-- Bootstrap CSS -->
    <link rel="stylesheet" href="https://stackpath.bootstrapcdn.com/bootstrap/4.3.1/css/bootstrap.min.css"
        integrity="sha384-ggOyR0iXCbMQv3Xipma34MD+dH/1fQ784/j6cY/iJTQUOhcWr7x9JvoRxT2MZw1T" crossorigin="anonymous">
    <!-- for footer icons  -->
    <script src='https://kit.fontawesome.com/a076d05399.js' crossorigin='anonymous'></script>
    <!-- j query -->
    <script src="https://ajax.googleapis.com/ajax/libs/jquery/3.6.0/jquery.min.js"></script>
    <script src="https://cdnjs.cloudflare.com/ajax/libs/printThis/1.15.0/printThis.js"
        integrity="sha512-Fd3EQng6gZYBGzHbKd52pV76dXZZravPY7lxfg01nPx5mdekqS8kX4o1NfTtWiHqQyKhEGaReSf4BrtfKc+D5w=="
        crossorigin="anonymous" referrerpolicy="no-referrer"></script>

    <title>E-summit 23</title>
</head>

<body>

    <style>
    #canvas {
        display: none;
    }

    .hideprint {
        display: block;
    }

    @media print {

        /* hide every other element */
        body * {
            visibility: hidden;

        }

        .hideprint {
            display: none;
        }

        /* displaying only container element  */
        #canvas,
        .printelem * {
            display: block;
            margin-top: 50px;
            visibility: visible;
        }
    }
    </style>

    <nav class="navbar navbar-expand-lg navbar-dark bg-dark">
        <a class="navbar-brand" href="#">VEDC</a>
        <button class="navbar-toggler" type="button" data-toggle="collapse" data-target="#navbarNavDropdown"
            aria-controls="navbarNavDropdown" aria-expanded="false" aria-label="Toggle navigation">
            <span class="navbar-toggler-icon"></span>
        </button>
        <div class="collapse navbar-collapse" id="navbarNavDropdown">
            <ul class="navbar-nav">
                <li class="nav-item active">
                    <a class="nav-link" href="#">Home <span class="sr-only">(current)</span></a>
                </li>
                <li class="nav-item">
                    <a class="nav-link" href="register.php">Register</a>
                </li>
                <li class="nav-item">
                    <a class="nav-link" href="login.php">Login</a>
                </li>
                <li class="nav-item">
                    <a class="nav-link" href="logout.php">Logout</a>
                </li>



            </ul>

            <div class="navbar-collapse collapse">
                <ul class="navbar-nav ml-auto">
                    <li class="nav-item active">
                        <a class="nav-link" href="#"> <img src="https://img.icons8.com/metro/26/000000/guest-male.png">
                            <?php echo "Welcome ". $_SESSION['username']?></a>
                    </li>
                </ul>
            </div>


        </div>
    </nav>

    <div class="container mt-4">
        <h3><?php echo "Welcome ". $_SESSION['username']?> Here is your Ticket</h3>
        <hr>

    </div>

    <!-- ticket -->
    <div class="wrapper text-center hideprint">
        <img src="../images/Esummit.png" class="img-fluid" alt="E SUMMIT">
    </div>
    <!-- content -->
    <div class="container my-4 pt-xl-5 pb-xl-5 printelem">
        <div class="row featurette d-flex justify-content-center align-items-center">
            <div class="col">
                <h1 class="display-3 text-center">Brought To You By</h1>
            </div>
            <div class="col-md-6">
                <img class="img-fluid" src="../images/logo.png" alt="VEDC Vit Pune">
            </div>
        </div>
    </div>
    <div class="container pt-xl-5 pb-xl-5 text-center">
        <div class="row pt-xl-5 pb-xl-5">
            <h1 class="display-6 text-center">Below is your ticket for the Event</h1>
        </div>
    </div>
    <div class="container pt-xl-5 pb-xl-5 text-center">
        <div class="row pt-xl-5 pb-xl-5">
            <!-- svg -->
            <!-- <div id = "svg-container"> -->
            <?xml version="1.0" encoding="utf-8"?>
            <!-- Generator: Adobe Illustrator 26.0.0, SVG Export Plug-In . SVG Version: 6.00 Build 0)  -->
            <svg version="1.1" id="Layer_1" xmlns="http://www.w3.org/2000/svg"
                xmlns:xlink="http://www.w3.org/1999/xlink" x="0px" y="0px" viewBox="0 0 612 201.6"
                style="enable-background:new 0 0 612 201.6;" xml:space="preserve">
                <style type="text/css">
                .st0 {
                    fill: none;
                }

                .st1 {
                    fill: #FFFFFF;
                }

                .st2 {
                    font-family: 'MyriadPro-Regular';
                }

                .st3 {
                    font-size: 12px;
                }

                .st4 {
                    fill: #E6332A;
                }

                .st5 {
                    font-size: 7.2054px;
                }

                .st6 {
                    fill: #E30613;
                }

                .st7 {
                    font-size: 37.8599px;
                }

                .st8 {
                    opacity: 0.78;
                    fill: #FFFFFF;
                }

                .st9 {
                    font-size: 8px;
                }

                .st10 {
                    font-size: 9px;
                }
                </style>
                <rect y="0" width="490.4" height="201.6" />
                <rect x="207.8" y="33.7" class="st0" width="85.5" height="10.3" />
                <text transform="matrix(1 0 0 1 207.7598 42.2138)" class="st1 st2 st3">VEDC PRESENTS</text>
                <rect x="490.4" class="st4" width="121.6" height="201.6" />
                <text transform="matrix(1.2755 0 0 1 207.7599 61.4473)" class="st1 st2 st5">THE ABYSS OF
                    ADROITNESS</text>
                <rect x="205.5" y="77.5" class="st0" width="209" height="28.8" />
                <text transform="matrix(0.7924 0 0 1 205.48 104.377)" class="st6 st2 st7">E - SUMMIT ’23</text>
                <rect x="207.8" y="120.6" class="st8" width="181.4" height="1.6" />
                <text transform="matrix(1 0 0 1 207.7508 138.5189)" class="st1 st2 st9">NOVEMBER 2, 2023</text>
                <text transform="matrix(1 0 0 1 290.1673 138.5186)" class="st1 st2 st9">SHARAD ARENA</text>
                <text transform="matrix(1 0 0 1 356.3345 138.5187)" class="st1 st2 st9">3- 5 PM</text>
                <text transform="matrix(0 -0.7237 1 0 557.3142 194.3068)" class="st1 st2 st10">TICKET :
                    <?php echo $finaluid?></text>
                <image style="overflow:visible;" width="271" height="304" xlink:href="../images/E.png"
                    transform="matrix(0.5543 0 0 0.4863 14.8931 19.6624)">
                </image>
                <image style="overflow:visible;" width="271" height="304" xlink:href="../images/E.png"
                    transform="matrix(0.4125 0 0 0.3722 495.3243 5.6098)">
                </image>
            </svg>
        </div>
        <!-- svg ends -->
    </div>
    </div>
    <div class="container mt-xl-5 mt-lg-5 mt-md-4 mt-sm-4 pb-xl-5 text-center">
        <div class="row pt-xl-5 pb-xl-5 printelem">
            <canvas id="canvas" width="2250" height="350"></canvas>
            <!-- <div id="png-container"></div>  -->
            <img src="../images/back.png" class="img-fluid" alt="Ticket Back">
        </div>
    </div>

    <script>
    var svgString = new XMLSerializer().serializeToString(document.querySelector('svg'));

    var canvas = document.getElementById("canvas");
    var ctx = canvas.getContext("2d");
    var DOMURL = self.URL || self.webkitURL || self;
    var img = new Image();
    var svg = new Blob([svgString], {
        type: "image/svg+xml;charset=utf-8"
    });
    var url = DOMURL.createObjectURL(svg);
    img.onload = function() {
        ctx.drawImage(img, 0, 0);
        var png = canvas.toDataURL("image/png");
        document.querySelector('#png-container').innerHTML = '<img src="' + png + '"/>';
        DOMURL.revokeObjectURL(png);
    };
    img.src = url;
    </script>

    <div class="text-center my-4 py-5">
        <button onclick="window.print();" id="print" type="button" class="btn btn-outline-success">Print Ticket</button>
    </div>
    <div class="container mt-xl-5 mt-lg-5 mt-md-4 mt-sm-4 pb-xl-5 text-center">
        <div class="row pt-xl-5 pb-xl-5 printelem">
            <img src='https://chart.googleapis.com/chart?chs=300x300&cht=qr&chl=<?php echo "$validationtext" ?>&choe=UTF-8'
                class="image-fluid mx-auto" alt="QR code">
        </div>
    </div>
    <!-- ticket ends -->

    <!-- footer starts  -->
    <footer class="bg-dark text-center text-white">
        <!-- Grid container -->
        <div class="container p-4 pb-0">
            <!-- Section: Social media -->
            <section class="mb-4">
                <!-- Facebook -->
                <a class="btn btn-outline-light btn-floating m-1" href="#!" role="button"><i
                        class="fab fa-facebook-f"></i></a>

                <!-- Twitter -->
                <a class="btn btn-outline-light btn-floating m-1" href="#!" role="button"><i
                        class="fab fa-twitter"></i></a>

                <!-- Google -->
                <a class="btn btn-outline-light btn-floating m-1" href="#!" role="button"><i
                        class="fab fa-google"></i></a>

                <!-- Instagram -->
                <a class="btn btn-outline-light btn-floating m-1" href="#!" role="button"><i
                        class="fab fa-instagram"></i></a>

                <!-- Linkedin -->
                <a class="btn btn-outline-light btn-floating m-1" href="#!" role="button"><i
                        class="fab fa-linkedin-in"></i></a>

                <!-- Github -->
                <a class="btn btn-outline-light btn-floating m-1" href="#!" role="button"><i
                        class="fab fa-github"></i></a>
            </section>
            <!-- Section: Social media -->
        </div>
        <!-- Grid container -->

        <!-- Copyright -->
        <div class="text-center p-3" style="background-color: rgba(0, 0, 0, 0.2);">
            © 2023 Copyright:
            <a class="text-white" href="https://mdbootstrap.com/">Built For VEDC</a>
        </div>
        <!-- Copyright -->
    </footer>
    <!-- footer ends  -->
    <!-- Optional JavaScript -->
    <!-- jQuery first, then Popper.js, then Bootstrap JS -->
    <script src="https://code.jquery.com/jquery-3.3.1.slim.min.js"
        integrity="sha384-q8i/X+965DzO0rT7abK41JStQIAqVgRVzpbzo5smXKp4YfRvH+8abtTE1Pi6jizo" crossorigin="anonymous">
    </script>
    <script src="https://cdnjs.cloudflare.com/ajax/libs/popper.js/1.14.7/umd/popper.min.js"
        integrity="sha384-UO2eT0CpHqdSJQ6hJty5KVphtPhzWj9WO1clHTMGa3JDZwrnQq4sF86dIHNDz0W1" crossorigin="anonymous">
    </script>
    <script src="https://stackpath.bootstrapcdn.com/bootstrap/4.3.1/js/bootstrap.min.js"
        integrity="sha384-JjSmVgyd0p3pXB1rRibZUAYoIIy6OrQ6VrjIEaFf/nJGzIxFDsf4x0xIM+B07jRM" crossorigin="anonymous">
    </script>
</body>

</html>