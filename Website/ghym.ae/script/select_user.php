<?php
 include '.include';
 if ($_GET["service"] && $_GET["phone"]){
  $sql="select ".$_GET["service"]." from `ghym`.`user` where `phone`=".$_GET["phone"];
  $code=query($db,$sql,0);
  echo $code[0][0];
 }else{
  echo "Error";
 }
 $db->close();
?>
