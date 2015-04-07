<?php
      $conn=@mysql_connect("localhost",'root','root')or die("数据库连接失败！");
      mysql_select_db("injection",$conn) or die("您要选择的数据库不存在");
      $name=$_POST['username'];
      $pwd=$_POST['password'];
      $sql="select * from users where username='$name' and password='$pwd'";
      $result=mysql_query($sql);// or die(mysql_error());
      $arr=mysql_fetch_array($result);
      #$arr = $result;
      if(is_array($arr))
      {
            //header("Location:manager.php");
            echo "TRUE";
      }
      else
      {
            echo "FALSE";
      }
?>
