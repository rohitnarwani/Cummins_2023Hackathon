<?php
  if (isset($_POST["submit"]))
  {

    //$mobile=$_POST['message'];
    $mobileno=$_POST['mobile'];


$fields = array(
    "sender_id" => "TXTIND",
    "message" => "Your Order is Ready For  Picked up  -
                Regards MeDonate ",
    "route" => "v3",
    "numbers" => " $mobileno",
);

$curl = curl_init();

curl_setopt_array($curl, array(
  CURLOPT_URL => "https://www.fast2sms.com/dev/bulkV2",
  CURLOPT_RETURNTRANSFER => true,
  CURLOPT_ENCODING => "",
  CURLOPT_MAXREDIRS => 10,
  CURLOPT_TIMEOUT => 30,
  CURLOPT_SSL_VERIFYHOST => 0,
  CURLOPT_SSL_VERIFYPEER => 0,
  CURLOPT_HTTP_VERSION => CURL_HTTP_VERSION_1_1,
  CURLOPT_CUSTOMREQUEST => "POST",
  CURLOPT_POSTFIELDS => json_encode($fields),
  CURLOPT_HTTPHEADER => array(
    "authorization: WdhXcjOwEFMy9qtKVCvinJSpb87zeBQ2LHafRAsgU3uD1r4YPkxqirlZJbEkKRtP4mfOIDQ8eYH3Wy9d",
    "accept: */*",
    "cache-control: no-cache",
    "content-type: application/json"
  ),
));

$response = curl_exec($curl);
$err = curl_error($curl);

curl_close($curl);

if ($err) {
  echo "cURL Error #:" . $err;
} else {
  echo "<script> alert('Message Sent Successfully');window.location='/npodisplay.php' </script>";
}
  }


?>