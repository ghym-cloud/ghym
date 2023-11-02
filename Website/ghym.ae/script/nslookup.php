<?php
 include '.include';
 if ( isset($_GET["host"]) ) {
  echo shell_exec("nslookup ".$_GET["host"]." 172.16.0.8 | grep Address: | grep -v \# | sed --expression s/Address://");
 } elseif ( isset($_GET["ip"]) ) {
  echo $_GET["ip"];
 }
?>
