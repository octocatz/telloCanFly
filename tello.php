<!DOCTYPE html>
<html class='stripe_base'>
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width,initial-scale=1.0">
<title>tello</title>
<link rel="stylesheet" type="text/css" href="style.css">
</head>
<body class='stripe_base'>
<h1>tello</h1>
<h3>tello exec</h3>
<?php

$exec_cmd = "./Tello3_custom.py";
exec($exec_cmd,$out2,$ret2);

?>
/body>
</html>