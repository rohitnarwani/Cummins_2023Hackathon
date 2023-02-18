<!DOCTYPE html>
<html class="wide wow-animation" lang="en"> 
  <head>
    <title>Dinners of Desire</title>
    <meta charset="utf-8">
    <meta name="viewport" content="width=device-width, height=device-height, initial-scale=1.0">
    <meta http-equiv="X-UA-Compatible" content="IE=edge">
    <link rel="icon" href="images/banner/Favicon.png" type="image/x-icon">
    <link rel="stylesheet" type="text/css" href="//fonts.googleapis.com/css?family=Poppins:300,300i,400,500,600,700,800,900,900i%7CPT+Serif:400,700">
    <link rel="stylesheet" href="css/bootstrap.css">
    <link rel="stylesheet" href="css/fonts.css">
    <link rel="stylesheet" href="css/style.css">
    <!-- Font Awesome -->
<link
  href="https://cdnjs.cloudflare.com/ajax/libs/font-awesome/6.0.0/css/all.min.css"
  rel="stylesheet"
/>
<!-- Google Fonts -->
<link
  href="https://fonts.googleapis.com/css?family=Roboto:300,400,500,700&display=swap"
  rel="stylesheet"
/>
<!-- MDB -->
<link
  href="https://cdnjs.cloudflare.com/ajax/libs/mdb-ui-kit/6.1.0/mdb.min.css"
  rel="stylesheet"
/>
    <link href="https://cdn.jsdelivr.net/npm/bootstrap@5.0.2/dist/css/bootstrap.min.css" rel="stylesheet" integrity="sha384-EVSTQN3/azprG1Anm3QDgpJLIm9Nao0Yz1ztcQTwFspd3yD65VohhpuuCOmLASjC" crossorigin="anonymous">
    <style>.ie-panel{display: none;background: #212121;padding: 10px 0;box-shadow: 3px 3px 5px 0 rgba(0,0,0,.3);clear: both;text-align:center;position: relative;z-index: 1;} html.ie-10 .ie-panel, html.lt-ie-10 .ie-panel {display: block;}</style>
  </head>
  <style>
    .modal-body {
    position: relative;
    flex: 1 1 auto;
    padding: 1rem;
    font-size: larger;
    text-align: center;
}
  </style>
  <body>
   
      <header class="section page-header">
        <!-- RD Navbar-->
        <div class="rd-navbar-wrap">
          <nav class="rd-navbar rd-navbar-classic" data-layout="rd-navbar-fixed" data-sm-layout="rd-navbar-fixed" data-md-layout="rd-navbar-fixed" data-md-device-layout="rd-navbar-fixed" data-lg-layout="rd-navbar-static" data-lg-device-layout="rd-navbar-static" data-xl-layout="rd-navbar-static" data-xl-device-layout="rd-navbar-static" data-lg-stick-up-offset="46px" data-xl-stick-up-offset="46px" data-xxl-stick-up-offset="46px" data-lg-stick-up="true" data-xl-stick-up="true" data-xxl-stick-up="true">
            <div class="rd-navbar-main-outer">
              <div class="rd-navbar-main">
                <!-- RD Navbar Panel-->
                <div class="rd-navbar-panel"> 
                  <!-- RD Navbar Toggle-->
                  <button class="rd-navbar-toggle" data-rd-navbar-toggle=".rd-navbar-nav-wrap"><span></span></button>
                  <!-- RD Navbar Brand-->
                  <div class="rd-navbar-brand"><a href="index.html"><img class="brand-logo-light" src="images/banner/LOGO.png" alt="" width="140" height="57" srcset="images/banner/LOGO.png 2x"/></a></div>
                </div>
                <div class="rd-navbar-main-element">
                  <div class="rd-navbar-nav-wrap">
                    <!-- RD Navbar Nav-->
                    <ul class="rd-navbar-nav">
                      <li class="rd-nav-item active"><a class="rd-nav-link" href="index.html">Home</a>
                      </li>
                      <li class="rd-nav-item"><a class="rd-nav-link"href="about.html"  >About</a>
                      </li>
                   
                      
                    </ul><a class="button button-white button-sm" href="#">book now</a>
                  </div>
                </div>

               

             
                <button class="button button-white button-sm" type="submit"  onclick="location.href='/Cinema-Reservation/index.php'"   >book Table</button>
                <button class="button button-white button-sm" type="submit" data-mdb-toggle="modal" data-mdb-target="#exampleModal1"    >Admin</button>
                <button class="button button-white button-sm" type="submit"  onclick="location.href='Food_Ordering_System/index.php'"   >Order Food</button>
        
                
              </div>
            </div>
          </nav>
        </div>
      </header>
      <div class="modal fade" id="exampleModal1" tabindex="-1" aria-labelledby="exampleModalLabel" aria-hidden="true">
  <div class="modal-dialog modal-dialog-centered">
    <div class="modal-content">
      <div class="modal-header">
        <h5 class="modal-title" id="exampleModalLabel">Admin</h5>
        <button type="button" class="btn-close" data-mdb-dismiss="modal" aria-label="Close"></button>
      </div>
      <div class="modal-body"><button type="button" class="btn btn-primary"  onclick="location.href='Food_Ordering_System/admin/manage-order.php'">For Food</button>
        <button type="button" class="btn btn-primary"     onclick="location.href='Cinema-Reservation/admin/admin.php'">For Table</button></div>
      <div class="modal-footer">
      <button type="button" class="btn btn-secondary" data-mdb-dismiss="modal">Close</button>
      
      </div>
    </div>
  </div>
</div>
    




      <!-- Swiper-->
      <section class="section section-lg section-main-bunner section-main-bunner-filter text-center">
        <div class="main-bunner-img" style="background-image: url(images/banner/bg-1.jpg); background-size: cover;"></div>
        <div class="main-bunner-inner">
          <div class="container">
            <div class="box-default">
              <h1 class="box-default-title">Welcome</h1>
              <div class="box-default-decor"></div>
              <p class="big box-default-text">Welcome to Dinners of Desire, where we serve up delicious meals that will tantalize your taste buds and leave you fully satisfied.</p>
            </div>
          </div>
        </div>
      </section>
      <div class="bg-gray-1">
        <section class="section-transform-top">
          <div class="container">
            <div class="box-booking">
              <form class="rd-form rd-mailform booking-form">
                <div>
                  <p class="booking-title">Name</p>
                  <div class="form-wrap">
                    <input class="form-input" id="booking-name" type="text" name="name" data-constraints="@Required">
                    <label class="form-label" for="booking-name">Your name</label>
                  </div>
                </div>
                <div>
                  <p class="booking-title">Phone</p>
                  <div class="form-wrap">
                    <input class="form-input" id="booking-phone" type="text" name="phone" data-constraints="@Numeric">
                    <label class="form-label" for="booking-phone">Your phone number</label>
                  </div>
                </div>
                <div>
                  <p class="booking-title">Date</p>
                  <div class="form-wrap form-wrap-icon"><span class="icon mdi mdi-calendar-text"></span>
                    <input class="form-input" id="booking-date" type="text" name="date" data-constraints="@Required" data-time-picker="date">
                  </div>
                </div>
                <div>
                  <p class="booking-title">no. of people</p>
                  <div class="form-wrap">
                    <select data-placeholder="2">
                      <option label="placeholder"></option>
                      <option>1</option>
                      <option>2</option>
                      <option>3</option>
                      <option>4</option>
                      <option>5</option>
                      <option>6</option>
                      <option>7</option>
                    </select>
                  </div>
                </div>
                <div>
                  <button class="button button-lg button-gray-600" type="submit" data-mdb-toggle="modal" data-mdb-target="#exampleModal">Check availability</button>
                </div>
               


              </form>
            </div>
          </div>
        </section>
        <!-- Modal -->
<div class="modal fade" id="exampleModal" tabindex="-1" aria-labelledby="exampleModalLabel" aria-hidden="true">
  <div class="modal-dialog modal-dialog-centered">
    <div class="modal-content">
      <div class="modal-header">
        <h5  class="modal-title"  id="exampleModalLabel">Seats Available</h5>
        <button type="button" class="btn-close" data-mdb-dismiss="modal" aria-label="Close"></button>
      </div>
      <div class="modal-body">
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

// output the number of available seats

echo $availableSeats . ' Seats Available';

// close the database connection
mysqli_close($conn);
?>








      </div>
      <div class="modal-footer">
        <button type="button" class="btn btn-primary" data-mdb-dismiss="modal">Close</button>
       
      </div>
    </div>
  </div>
</div>
        <section class="section section-lg section-inset-1 bg-gray-1 pt-lg-0">
          <div class="container">
            <div class="row row-50 justify-content-xl-between align-items-lg-center">
              <div class="col-lg-6 wow fadeInLeft">
                <div class="box-image"><img class="box-image-static" src="images/banner/food6.jpg" alt="" width="483" height="327"/><img class="box-image-position" src="images/banner/food6.jpg" alt="" width="341" height="391"/>
                </div>
              </div>
              <div class="col-lg-6 col-xl-5 wow fadeInRight">
                <h2>About Us</h2>
                <p>Welcome to Dinners of Desire, the ultimate destination for foodies who crave a delicious and satisfying meal.</p>
                <p>Dinners of Desire provides an unparalleled dining experience with a commitment to reducing food waste and using only the freshest ingredients. </p>
                  <P style="color: gray;">  Book your table today and join us for a delicious and unforgettable meal that will leave you wanting more!</p>
              </div>
            </div>
          </div>
        </section>
      </div>
     
      <section class="section section-lg bg-gray-1">
        <div class="container">
          <h2 class="text-center">Our Restaurant Menu</h2>
          <div class="row">
            <div class="col-12">
              <div class="tabs-custom tabs-horizontal tabs-classic" id="tabs-1">
                <ul class="nav nav-tabs nav-tabs-classic">
                  <li class="nav-item" role="presentation"><a class="nav-link active" href="#tabs-1-1" data-toggle="tab">Features</a></li>
                  <li class="nav-item" role="presentation"><a class="nav-link" href="#tabs-1-2" data-toggle="tab">Desserts</a></li>
                  <li class="nav-item" role="presentation"><a class="nav-link" href="#tabs-1-3" data-toggle="tab">drinks</a></li>
                </ul>
                <div class="tab-content">
                  <div class="tab-pane fade show active" id="tabs-1-1">
                    
                    <div class="container">
               
                      <div class="row row-30 row-md-60">
                        <div class="col-md-6 col-lg-4">
                          <div class="box-icon-modern">
                            <div class="box-icon-inner decorate-triangle"><span class="icon-xl restaurant-icon-30"></span></div>
                            <div class="box-icon-caption">
                              <h4><a href="#">Friendly Team</a></h4>
                              <p>Our friendly staff is always ready to welcome you with a smile and ensure that you have an unforgettable dining experience.</p>
                            </div>
                          </div>
                        </div>
                        <div class="col-md-6 col-lg-4">
                          <div class="box-icon-modern">
                            <div class="box-icon-inner decorate-circle"><span class="icon-xl restaurant-icon-11"></span></div>
                            <div class="box-icon-caption">
                              <h4><a href="#">Fresh Food</a></h4>
                              <p>Our commitment to sourcing only the freshest ingredients ensures that every bite of our food </p>
                            </div>
                          </div>
                        </div>
                        <div class="col-md-6 col-lg-4">
                          <div class="box-icon-modern">
                            <div class="box-icon-inner decorate-rectangle"><span class="icon-xl restaurant-icon-36"></span></div>
                            <div class="box-icon-caption">
                              <h4><a href="#">Quality Cuisine</a></h4>
                              <p>We specialize in quality cuisine that is not only delicious, but also nutritious and healthy, using only the best ingredients available.</p>
                            </div>
                          </div>
                        </div>
                        <div class="col-md-6 col-lg-4">
                          <div class="box-icon-modern">
                            <div class="box-icon-inner decorate-circle"><span class="icon-xl restaurant-icon-27"></span></div>
                            <div class="box-icon-caption">
                              <h4><a href="#">Best Service</a></h4>
                              <p>We pride ourselves on providing the best service possible, making sure that every aspect of your dining experience is top-notch.</p>
                            </div>
                          </div>
                        </div>
                        <div class="col-md-6 col-lg-4">
                          <div class="box-icon-modern">
                            <div class="box-icon-inner decorate-triangle"><span class="icon-xl restaurant-icon-34"></span></div>
                            <div class="box-icon-caption">
                              <h4><a href="#">Advance Booking</a></h4>
                              <p>With our easy-to-use online booking system, you can secure your spot at Dinners of Desire in advance. </p>
                            </div>
                          </div>
                        </div>
                        <div class="col-md-6 col-lg-4">
                          <div class="box-icon-modern">
                            <div class="box-icon-inner decorate-rectangle"><span class="icon-xl restaurant-icon-26"></span></div>
                            <div class="box-icon-caption">
                              <h4><a href="#">Affordable Prices</a></h4>
                              <p>We offer delicious, high-quality meals at affordable prices, so that everyone can enjoy a fantastic dining experience at Dinners of Desire.</p>
                            </div>
                          </div>
                        </div>
                      </div>
                    </div>
                  </div>
                  <div class="tab-pane fade show" id="tabs-1-2">
                
                    <div class="menu-container">
                    <div class="menu-item">
                      <h4><a href="#">Pav-Bhaji</a></h4>
                      <img class="imgst" src="https://static.toiimg.com/thumb/80287813.cms?resizemode=4&width=1200" alt="">
                      <p>A popular Indian street food consisting of a spiced vegetable curry (bhaji) served with a soft bread roll (pav), often garnished with onions, coriander, and lemon</p>
                      <p class="event-time">&#8377 80</p>
                    </div>
                    <div class="menu-item">
                      <h4><a href="#">Burger</a></h4>
                      <img class="imgst" src="images/banner/burger.png" alt="">
                      <p>A popular fast food item made of a patty of ground meat, typically beef, served on a bun with various toppings such as lettuce, tomato, cheese, and condiments.</p>
                      <p class="event-time">&#8377 70</p>
                    </div>
                    <div class="menu-item">
                      <h4><a href="#">Masala Dosa</a></h4>
                      <img class="imgst" src="images/banner/masala-dosa.png" alt="">
                      <p>A South Indian crepe-like dish made from rice and lentil batter, filled with spiced potatoes and served with chutney and sambar.</p>
                      <p class="event-time">&#8377 60</p>
                    </div>
                    <div class="menu-item">
                      <h4><a href="#">Noodles</a></h4>
                      <img class="imgst" src="images/banner/noodle.png" alt="">
                      <p>A dish made from long, thin strips of dough, often served with a sauce or in a soup and may include various vegetables, meats, or seafood.</p>
                      <p class="event-time">&#8377 50</p>
                    </div>
                    <div class="menu-item">
                      <h4><a href="#">Veg Thali</a></h4>
                      <img class="imgst" src="images/banner/veg-thali.png" alt="">
                      <p>A traditional Indian meal consisting of various vegetarian dishes served on a platter, often accompanied by rice, bread, and dessert.</p>
                      <p class="event-time">&#8377 80</p>
                    </div>
                    <div class="menu-item">
                      <h4><a href="#">Pizza</a></h4>
                      <img class="imgst" src="images/banner/pizza.png" alt="">
                      <p>A savory dish typically made of a dough crust, tomato sauce, cheese, and various toppings, and baked in an oven.</p>
                      <p class="event-time">&#8377 70</p>
                    </div>
                    </div>
                  </div>
              
                  <div class="tab-pane fade" id="tabs-1-3">
                    <div class="menu-container">
                     <div class="menu-item">
                       <h4><a href="#">Sprite</a></h4>
                       <img class="imgst" src="https://5.imimg.com/data5/UE/NE/WQ/SELLER-82456434/sprinte-cold-derink-500x500.jpg" alt="">
                       <p>Sprite is a colorless, lemon-lime flavored soft drink.</p>
                       <p class="event-time">&#8377 20</p>
                     </div>
                     <div class="menu-item">
                       <h4><a href="#">Cold Coffee</a></h4>
                       <img class="imgst" src="https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcQPjwGIgIHeL_6IPRL-xZG3X7hlsvb5U7qT0w&usqp=CAU" alt="">
                       <p>Cold coffee, also known as iced coffee, is a chilled coffee beverage that is typically served with ice and may be sweetened and/or flavored.</p>
                       <p class="event-time">&#8377 40</p>
                     </div>
                     <div class="menu-item">
                       <h4><a href="#">Coco-Cola</a></h4>
                       <img class="imgst" src="https://www.jiomart.com/images/product/original/491121060/coca-cola-1-75-l-product-images-o491121060-p491121060-0-202206022121.jpg" alt="">
                       <p>Coca-Cola is a carbonated soft drink produced by The Coca-Cola Company, known for its distinctive caramel color and sweet, fizzy taste.</p>
                       <p class="event-time">&#8377 20</p>
                     </div>
                     <div class="menu-item">
                       <h4><a href="#">Bisleri</a></h4>
                       <img class="imgst" src="https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcS72g-Jyi8yABwWgvOSwY7CVw3otvcmHXI79w&usqp=CAU" alt="">
                       <p>A water bottle is a container designed for carrying water or other beverages while on-the-go, often made of plastic, metal, or glass.</p>
                       <p class="event-time">&#8377 20</p>
                     </div>
                     <div class="menu-item">
                       <h4><a href="#">Green Tea</a></h4>
                       <img class="imgst" src="https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcToXrXmNOjk-6qRaO40IfdxJP81IkTfvvJp8g&usqp=CAU" alt="">
                       <p>Green tea is a type of tea made from unfermented leaves that are minimally processed, known for its light, fresh flavor and numerous health benefits.</p>
                       <p class="event-time">&#8377 30</p>
                     </div>
                     <div class="menu-item">
                       <h4><a href="#">Papaya Juice</a></h4>
                       <img class="imgst" src="https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcQqnUYM4ihzCv1E7tWvNvK9kwFXjJY-3PFjSQ&usqp=CAU" alt="">
                       <p>Papaya juice is a sweet and refreshing beverage made from the pulp of the tropical papaya fruit.</p>
                       <p class="event-time">&#8377 50</p>
                     </div>
                     </div>
                   </div>
                 
                </div>
              </div>
            </div>
          </div>
        </div>
      </section>
     
      




<!-- images -->
<script src="https://cdn.jsdelivr.net/npm/bootstrap@5.3.0-alpha1/dist/js/bootstrap.bundle.min.js" integrity="sha384-w76AqPfDkMBDXo30jS1Sgez6pr3x5MlQ1ZAGC+nuZB+EYdgRZgiwxhTBTkF7CXvN" crossorigin="anonymous"></script>

      <!-- Page Footer-->
      <!-- Remove the container if you want to extend the Footer to full width. -->

  <!-- Footer -->
  <footer
          class="text-center text-lg-start text-white"
          style="background-color: #929fba"
          >
    <!-- Grid container -->
    <div class="container p-4 pb-0">
      <!-- Section: Links -->
      <section class="">
        <!--Grid row-->
        <div class="row">
          <!-- Grid column -->  
          <div class="col-md-3 col-lg-3 col-xl-3 mx-auto mt-3">
            <!-- <img style="max-width: 45%;" src="images/banner/LOGO.png" alt=""> -->

            <style >
              .a{
                line-height: 1.6;
                font-weight: bold;
              }
              .a1{
                line-height: 1.6;
                font-weight: bold;
                font-family: cursive;

              }
            </style>
            <div class="a">ONE CANNOT</div>
            <div style="color: black;" class="a">THINK WELL,</div>
            <div style="color:black" class="a">LOVE WELL,</div>
            <div style="color:black" class="a">SLEEP WELL,</div>
            <div class="a">IF ONE HAS NOT</div>
            <div style="color: black" class="a1">Dined Well</div>
          </div>
          <!-- Grid column -->

          <hr class="w-100 clearfix d-md-none" />

         
          <!-- Grid column -->

          <hr class="w-100 clearfix d-md-none" />

          <!-- Grid column -->
          <hr class="w-100 clearfix d-md-none" />

          <!-- Grid column -->
          <div class="col-md-4 col-lg-3 col-xl-3 mx-auto mt-3">
            <h6 class="text-uppercase mb-4 font-weight-bold">Contact</h6>
            <p><i class="fas fa-home mr-3"></i> Pune, Maharashtra, India.</p>
            <p><i class="fas fa-envelope mr-3"></i> shantanu.wadode21@vit.edu</p>
            <p><i class="fas fa-phone mr-3"></i> +91 9405267368</p>
            <p><i class="fas fa-print mr-3"></i> +91 9579535345</p>
          </div>
          <!-- Grid column -->

          <!-- Grid column -->
          <div class="col-md-3 col-lg-3 col-xl-2 mx-auto mt-3">
            <h6 class="text-uppercase mb-4 font-weight-bold">Follow us</h6>

            <!-- Facebook -->
            <a
               class="btn  btn-floating m-1"
              
               href="#!"
               role="button"
               ><img src="images/banner/facebook_icon-icons.com_53612.png" alt="">
              </a>

            <!-- Twitter -->
            <a
               class="btn  btn-floating m-1"
              
               href="#!"
               role="button"
               ><img src="images/banner/1491579583-yumminkysocialmedia02_83111.png" alt="">
              </a>

            <!-- Google -->
            <a
            class="btn  btn-floating m-1"
           
            href="#!"
            role="button"
            ><img src="images/banner/Google_icon-icons.com_66793.png" alt="">
           </a>

            <!-- Instagram -->
            <a
               class="btn  btn-floating m-1"
              
               href="#!"
               role="button"
               ><img src="images/banner/3721672-instagram_108066.png" alt="">
              </a>

            <!-- Linkedin -->
            <a
               class="btn  btn-floating m-1"
              
               href="#!"
               role="button"
               ><img src="images/banner/linkedin_socialnetwork_17441.png" alt="">
              </a>
            <!-- Github -->
            <a
               class="btn  btn-floating m-1"
              
               href="#!"
               role="button"
               ><img src="images/banner/github_original_wordmark_logo_icon_146506.png" alt="">
              </a>
          </div>
        </div>
        <!--Grid row-->
      </section>
      <!-- Section: Links -->
    </div>
    <!-- Grid container -->

    <!-- Copyright -->
    <div
         class="text-center p-3"
         style="background-color: rgba(0, 0, 0, 0.2)"
         >
    <b>Designed By Titans✨✨</b>
      
    </div>
    <!-- Copyright -->
  </footer>
  <!-- Footer -->

<!-- End of .container -->
<!-- MDB -->
<script
  type="text/javascript"
  src="https://cdnjs.cloudflare.com/ajax/libs/mdb-ui-kit/6.1.0/mdb.min.js"
></script>
      
    
    <div class="snackbars" id="form-output-global"></div>
    <script src="js/core.min.js"></script>
    <script src="js/script.js"></script>
  </body>
</html>