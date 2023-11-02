<?php
 include '.include';
 $sql="update `ghym`.`user` set `active`=1".(($_GET["git"])?",`git`=".$_GET["git"]:"").(($_GET["vm"])?",`vm`=".$_GET["vm"]:"").(($_GET["k8s"])?",`k8s`=".$_GET["k8s"]:"").(($_GET["apache"])?",`apache`=".$_GET["apache"]:"").(($_GET["nginx"])?",`nginx`=".$_GET["nginx"]:"").(($_GET["mysql"])?",`mysql`=".$_GET["mysql"]:"").(($_GET["postgresql"])?",`postgresql`=".$_GET["postgresql"]:"").(($_GET["mongodb"])?",`mongodb`=".$_GET["mongodb"]:"").(($_GET["redis"])?",`redis`=".$_GET["redis"]:"").(($_GET["cassandra"])?",`cassandra`=".$_GET["cassandra"]:"").(($_GET["kafka"])?",`kafka`=".$_GET["kafka"]:"").(($_GET["s3"])?",`s3`=".$_GET["s3"]:"").(($_GET["fs"])?",`fs`=".$_GET["fs"]:"").(($_GET["prometheus"])?",`prometheus`=".$_GET["prometheus"]:"").(($_GET["zabbix"])?",`zabbix`=".$_GET["zabbix"]:"")." where `phone`=".$_GET["phone"];
 if (mysqli_query($db,$sql)){
  echo "OK";
 }else{
  die(mysqli_error());
  echo "Error";
 }
 $db->close();
?>
