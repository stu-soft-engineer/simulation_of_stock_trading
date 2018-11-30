<%@ page language="java" import="java.sql.*" import="java.util.*" import="utils.DBConn;" contentType="text/html; charset=UTF-8"
    pageEncoding="UTF-8"%>
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
    <title>Insert title here</title>
</head>
<body>
    <div id="head">						<!--  点击左上角的图标按钮可以返回到Match.jsp的主页 -->
        <div class="container">
            <div class="row">

              <div class="col-lg-4 col-md-4 col-sm-4">
                    <a href="Match.hsp">
                    <img src="assets/img/logo1.png"  />
                </a>
                </div>
            </div>
        </div>
    </div>
    
    <section id="main" >
        <div class="container" >
            <div class="row">
                <div class="col-lg-9 col-md-9 col-sm-9">
 <div class="panel panel-default">
  <div class="panel-body">
	<%
	String _match_id=request.getParameter("id");				//通过url来获取id号
	System.out.print(_match_id);
	int match_id=Integer.parseInt(_match_id);					//字符型转换成整型
	Statement state=null;
	ResultSet rs=null;
	Connection conn=null;
	try {
		DBConn db=new DBConn();								//连接数据库的操作
		conn=db.getConn();
		state=conn.createStatement();
		rs=state.executeQuery("select *from match_db");		//根据sql语句查询并返回一个结果集
		int count=0;
		while(rs.next()){
			if(match_id==rs.getInt(1)){
				String match_name=rs.getString("match_name");		//从结果集中获取需要的信息
				String regist_time=rs.getString("regist_time");
				String start_time=rs.getString("start_time");
				String introduction=rs.getString("introduction");
				String rules=rs.getString("rules");
				String end_time=rs.getString("end_time");
				String init_money=rs.getString("init_money");
			%>
						<div>
                      		<label>比赛名称</label>				<!--  显示信息 -->
							<p><%=match_name %></p>
                        </div>
                        <div>
                            <label>简介</label>
                            <p><%=introduction %></p>
                        </div>
                        <div>
                            <label>开始时间</label>
                            <p><%=start_time %></p>
                        </div>
                        <div>
                            <label>结束时间</label>
                            <p><%=end_time %></p>
                        </div>
                         <div>
                            <label>初始金额</label>
                            <p><%=init_money %></p>
                        </div>
                        <div>
                            <label>规则</label>
                            <p><%=rules %></p>
                        </div>
			<%
			}
		}
	}catch(Exception e){
		e.printStackTrace();
	}finally{
		try{	
			if(rs!=null)			//连接完记得要关闭
				rs.close();
			if(state!=null)
				state.close();
			if(conn!=null)
				conn.close();
		}catch(SQLException e){
			e.printStackTrace();
		}
	}
	
	%>
  </div>
</div>
 </div>
                        <div class="col-lg-3 col-md-3 col-sm-3">
<div class="list-group">
	<a href="changeMatch.jsp?id=<%=match_id %>" class="list-group-item active">修改该比赛</a>		<!--  页面的跳转 -->
	<a href="deleteMatch.jsp?id=<%=match_id %>" class="list-group-item">删除该比赛</a>
 	 <a href="Match.jsp" class="list-group-item">返回首页</a>
</div>   
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

    