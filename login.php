<html>
<head>
<title>登录验证</title>
<meta http-equiv="content-type"content="text/html;charset=utf-8">
</head>
<body>
<?php
      $conn=@mysql_connect("localhost",'root','root')or die("数据库连接失败！");
      mysql_select_db("injection",$conn) or die("您要选择的数据库不存在");
      $name=$_POST['username'];
      $pwd=$_POST['password'];
      $sql="select * from users where username='$name' and password='$pwd'";
      $result=mysql_query($sql) or die(mysql_error());




      $arr=mysql_fetch_array($result);
      if(is_array($arr))
      {
            header("Location:manager.php");
      }
      else
      {
            echo "您的用户名或密码输入有误";
      }
?>
</body>
</html>