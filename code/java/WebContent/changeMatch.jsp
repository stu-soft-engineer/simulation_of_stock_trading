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
    <title>修改公告</title>
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
    <div id="head">						<!-- 与addMatch同理 -->
        <div class="container">
            <div class="row">

              <div class="col-lg-4 col-md-4 col-sm-4">
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
					
                    <h3 class=" text-center">修改比赛</h3>
                   <div class="hr-div"> <hr /></div>
                    <form action="MatchesServlet" method="post">
                    <!-- <%
							//String id=request.getParameter("id");
							//System.out.println(id);
							%> -->	
                   <%
	String _match_id=request.getParameter("id");				//通过url来获取id号
	System.out.print(_match_id);
	int id=Integer.parseInt(_match_id);					//字符型转换成整型
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
			if(id==rs.getInt(1)){
				String match_name=rs.getString("match_name");		//从结果集中获取需要的信息
				String sign_time = new java.text.SimpleDateFormat("yyyy-MM-dd HH:mm:ss").format(new java.util.Date(Long.valueOf((rs.getInt("sign_time")) * 1000L)));
				String start_time = new java.text.SimpleDateFormat("yyyy-MM-dd HH:mm:ss").format(new java.util.Date(Long.valueOf((rs.getInt("start_time")) * 1000L)));
				String match_detail=rs.getString("match_detail");
				String match_rule=rs.getString("match_rule");
				String end_time = new java.text.SimpleDateFormat("yyyy-MM-dd HH:mm:ss").format(new java.util.Date(Long.valueOf((rs.getInt("end_time")) * 1000L)));
				
				int init_money=rs.getInt("init_money");
			%>
                         <div class="form-group col-lg-12 col-md-12 col-sm-12">
                            <label>比赛名称</label>  
							<input type="text" name="match_name" class="form-control" required="required" value="<%=match_name %>"/>
                        </div> 	
                        <div class="form-group col-lg-12 col-md-12 col-sm-12">
                            <label>比赛详情</label>
                            <input type="text" name="match_detail" class="form-control" required="required" value="<%=match_detail %>"/>
                        </div>
                        <div class="form-group col-lg-12 col-md-12 col-sm-12">
                            <label>开始时间</label>
                            <input type="text" name="start_time" class="form-control" required="required" value="<%=start_time%>"/>
                        </div>
                        <div class="form-group col-lg-12 col-md-12 col-sm-12">
                            <label>结束时间</label>
                            <input type="text" name="end_time" class="form-control" required="required" value="<%=end_time%>"/>
                        </div>
                         <div class="form-group col-lg-12 col-md-12 col-sm-12">
                            <label>初始金额</label>
                            <input type="text" name="init_money" class="form-control" required="required" value="<%=init_money %>"/>
                        </div>
                        <div class="form-group col-lg-12 col-md-12 col-sm-12">
                            <label>规则</label>
                            <textarea class="form-control" name="match_rule" rows="14" ><%=match_rule %></textarea>
                            <script type="text/javascript">CKEDITOR.replace('match_rule');</script>
                        </div>
						<input type="hidden" name="action" value="change"/>
						<input type="hidden" name="id" value="<%=id %>"/>
                        <div class="form-group col-lg-12 col-md-12 col-sm-12">
                            <button type="submit" class="btn btn-primary">修改比赛</button>
                        </div>
                    </form>
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
    </section>
    <!--  Jquery Core Script -->
    <script src="assets/js/jquery-1.10.2.js"></script>
    <!--  Core Bootstrap Script -->
    <script src="assets/js/bootstrap.js"></script>

</body>
</html>
