<?php
 include '.include';
 if ($_GET["port"]){
  $sql="select count(*) from `ghym`.`port` where `port`=".$_GET["port"];
  $code=query($db,$sql,0);
  echo $code[0][0];
 }else{
  echo "Error";
 }
 $db->close();
?>
