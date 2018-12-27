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
    <script type="text/javascript">
var currentpage = 1;
var pagesize = 10;
function goPage(num){
	var table = document.getElementById("Matches");
	var rows = table.rows.length-1;
	currentpage = num;
	if (currentpage == 0) currentpage = 1;
	if (currentpage == parseInt(rows/pagesize)+2)currentpage = parseInt(rows/pagesize)+1;
	for(var a=1;a<rows+1;a++){
		var row = document.getElementById(a.toString());
		if( a<=pagesize*(currentpage-1) || a>pagesize*currentpage ){row.style.display = "none"}
		else row.style.display = "table-row";
	}
}
	</script>
</head>
<body onload="goPage(1);">					<!-- 与Match同理 -->
    <div id="head">
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
    <section id="main" >
        <div class="container" >
            <div class="row">
                <div class="col-lg-9 col-md-9 col-sm-9">
                 
                   <h3>用户个人参加比赛详情</h3>
                     <div class="hr-div"> <hr /></div>
                            <div class="table-responsive">
                                <table class="table table-striped table-bordered table-hover" id="Matches" >
                                    <thead>
                                        <tr>
                                            <th width="10%"> <div align="center">ID</div></th>
                                            <th width="18%"><div align="center">比赛ID</div></th>              
                                            <th width="18%"><div align="center">股票代码</div></th>
                                            <th width="18%"><div align="center">持所持股</div></th> 
                                            <th width="18%"><div align="center">股票价格</div></th> 
                                            <th width="18%"><div align="center">等待出售</div></th>    
                                        </tr>
                                    </thead>
                                    <tbody>
    <%
	String _user_wxid=request.getParameter("wxid");				//通过url来获取id号
	System.out.print(_user_wxid);
	String user_wxid = _user_wxid;					
	Statement state=null;
	ResultSet rs=null;
	Connection conn=null;
	try {
		DBConn db=new DBConn();								//连接数据库的操作
		conn=db.getConn();
		state=conn.createStatement();
		rs=state.executeQuery("select *from storage_db where wxid='"+user_wxid+"' ");		//根据sql语句查询并返回一个结果集
		int count=0;
		while(rs.next()){	
				String match_id=rs.getString("match_id");		//从结果集中获取需要的信息
				String stock_id = rs.getString("stock_id");
				String own_num = rs.getString("own_num");
				String ave_price = rs.getString("ave_price");
				String lock_num=rs.getString("lock_num");
				
			%>
			 <tr id="<%=count++%>" >
                <td><div align="center"><%=count%></div></td>
                <td class="td<%=count%>"><div align="center"><span class="label label-danger"><%=match_id %></span></div></td>
                <td class="td<%=count%>"><%=stock_id %></td>
                <td class="td<%=count%>"><%=own_num%></td>
                <td class="td<%=count%>"><%=ave_price %></td>
                <td class="td<%=count%>"><%=lock_num%></td>
           </tr>
		<%				
	//	}
		
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
                            		</tbody>
                                </table>                             
                            	<button  onclick="goPage(currentpage-1);">上一页</button>
                            	<button  onclick="goPage(currentpage+1);">下一页</button>
                            </div>                                           
                    </div>
                <div class="col-lg-3 col-md-3 col-sm-3">
<div class="list-group">
  <a href="Match.jsp" class="list-group-item active">
 	 查看比赛
  </a>
  <a href="log.jsp" class="list-group-item">查看日志</a>
  <a href="blacklist.jsp" class="list-group-item">查看用户黑名单</a>
</div>   
            </div>

        </div>

    </div>
    <!--  Jquery Core Script -->
    <script src="assets/js/jquery-1.10.2.js"></script>
    <!--  Core Bootstrap Script -->
    <script src="assets/js/bootstrap.js"></script>
</section>
</body>
</html>
