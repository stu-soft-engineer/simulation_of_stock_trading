<%@ page language="java" import="java.sql.*" import="java.util.*" import="utils.DBConn;" contentType="text/html; charset=UTF-8"
    pageEncoding="UTF-8"%>
<!--
//-->
</script>
<!DOCTYPE html>
<!--[if lt IE 7 ]><html class="ie ie6" lang="en"> <![endif]-->
<!--[if IE 7 ]><html class="ie ie7" lang="en"> <![endif]-->
<!--[if IE 8 ]><html class="ie ie8" lang="en"> <![endif]-->
<!--[if (gte IE 9)|!(IE)]><!-->
<html lang="en">
<!--<![endif]-->
<head>
    <meta charset="utf-8" />
    <meta name="viewport" content="width=device-width, initial-scale=1, maximum-scale=1" />
    <meta name="description" content="" />
    <meta name="author" content="" />
    <!--[if IE]>
        <meta http-equiv="X-UA-Compatible" content="IE=edge,chrome=1">
        <![endif]-->
    <title>Support Admin</title>
    <!-- BOOTSTRAP CORE STYLE CSS -->
    <link href="assets/css/bootstrap.css" rel="stylesheet" />
    <!-- FONT AWESOME CSS -->
    <link href="assets/css/font-awesome.min.css" rel="stylesheet" />
    <!-- CUSTOM STYLE CSS -->
    <link href="assets/css/style.css" rel="stylesheet" />
    <!-- Google	Fonts -->
    <link href='http://fonts.googleapis.com/css?family=Nova+Flat' rel='stylesheet' type='text/css' />
    <link href='http://fonts.googleapis.com/css?family=Open+Sans:400,700,300' rel='stylesheet' type='text/css' />
    <!-- HTML5 shim and Respond.js IE8 support of HTML5 elements and media queries -->
    <!--[if lt IE 9]>
      <script src="https://oss.maxcdn.com/libs/html5shiv/3.7.0/html5shiv.js"></script>
      <script src="https://oss.maxcdn.com/libs/respond.js/1.3.0/respond.min.js"></script>
    <![endif]-->
    <script type="text/javascript" src="resources/ckeditor/ckeditor.js"></script>
</head>
<body>
    <div id="head">									
        <div class="container">
            <div class="row">

              <div class="col-lg-4 col-md-4 col-sm-4">		<!-- 类名是为了增加css样式 -->
                    <a href="Match.jsp">
                    <img src="assets/img/logo1.png"  />
                  </a>
                </div>
            </div>
        </div>
    </div>
    <section>
        <div class="container">
            <div class="row noti-div"></div>


        </div>

    </section>
    <section id="main">
        <div class="container">
            <div class="row">
                <div class="col-lg-9 col-md-9 alert alert-info">		

                    <h3 class=" text-center">新增比赛</h3>
                   <div class="hr-div"> <hr /></div>
                    <form action="MatchesServlet" method="post">
                      <div class="form-group col-lg-12 col-md-12 col-sm-12">
                            <label>比赛名称</label>
							<input type="text" name="match_name" class="form-control" required="required"/>
                        </div>
                        <div class="form-group col-lg-12 col-md-12 col-sm-12">
                            <label>简介</label>
                            <input type="text" name="introduction" class="form-control" required="required"/>
                        </div>
                        <div class="form-group col-lg-12 col-md-12 col-sm-12">
                            <label>开始时间</label>
                            <input type="text" name="start_time" class="form-control" required="required"/>
                        </div>
                        <div class="form-group col-lg-12 col-md-12 col-sm-12">
                            <label>结束时间</label>
                            <input type="text" name="end_time" class="form-control" required="required"/>
                        </div>
                         <div class="form-group col-lg-12 col-md-12 col-sm-12">
                            <label>初始金额</label>
                            <input type="text" name="init_money" class="form-control" required="required"/>
                        </div>
                        <div class="form-group col-lg-12 col-md-12 col-sm-12">
                            <label>规则</label>
                            <textarea class="form-control" name="rules" rows="14"></textarea>
                            <script type="text/javascript">CKEDITOR.replace('rules');</script>
                        </div>
						<input type="hidden" name="action" value="insert"/>		<!-- 传递要做的操作和id号 -->
                        <div class="form-group col-lg-12 col-md-12 col-sm-12">
                            <button type="submit" class="btn btn-primary">发布比赛</button>
                        </div>
                    </form>

                </div>
          </div>
      </div>
    </section>
    <!--  Jquery Core Script -->
    <script src="assets/js/jquery-1.10.2.js"></script>
    <!--  Core Bootstrap Script -->
    <script src="assets/js/bootstrap.js"></script>
</body>
</html>
