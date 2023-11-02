<?php
 include '.include';
 $sql="insert into `ghym`.`port`(`port`,`type`) values (".$_GET['port'].",'".$_GET['type']."')";
 if (mysqli_query($db,$sql)){
  echo "OK";
 }else{
  die(mysqli_error());
  echo "Error";
 }
 $db->close();
?>
