package controller.matchesinfo;

import java.io.IOException;
import java.io.PrintWriter;
import java.net.URLEncoder;

import javax.servlet.RequestDispatcher;
import javax.servlet.ServletException;
import javax.servlet.http.HttpServlet;
import javax.servlet.http.HttpServletRequest;
import javax.servlet.http.HttpServletResponse;

import bean.newsinfo.MatchesInfoDAO;

import java.sql.*;

import utils.DBConn;

/**
 * Servlet implementation class AddMatchesAction
 */
public class AddMatchesAction extends HttpServlet {
	private static final long serialVersionUID = 1L;
       
    /**
     * @see HttpServlet#HttpServlet()
     */
    public AddMatchesAction() {
        super();
        // TODO Auto-generated constructor stub
    }

	/**
	 * @see HttpServlet#doGet(HttpServletRequest request, HttpServletResponse response)
	 */
	protected void doGet(HttpServletRequest request, HttpServletResponse response) throws ServletException, IOException {
		// TODO Auto-generated method stub
		doPost(request, response);  
	}

	/**
	 * @see HttpServlet#doPost(HttpServletRequest request, HttpServletResponse response)
	 */
	protected void doPost(HttpServletRequest request, HttpServletResponse response) throws ServletException, IOException {
		// TODO Auto-generated method stub
		PrintWriter out=response.getWriter();
		response.setHeader("content-type", "text/html;charset=UTF-8");  
		response.setCharacterEncoding("UTF-8");  
		request.setCharacterEncoding("UTF-8"); 
		String match_name=request.getParameter("match_name");  
        String introduction=request.getParameter("introduction");  
        String start_time=request.getParameter("start_time");
        String end_time=request.getParameter("end_time");
        String rules=request.getParameter("rules");
        String init_money=request.getParameter("init_money");
        String id=request.getParameter("id");
        String action=request.getParameter("action");
        
        if(action.equals("insert")){
            MatchesInfoDAO nid=new MatchesInfoDAO();
            boolean isMatchesInfo=nid.insert(match_name,introduction,start_time,end_time,rules,init_money);
//            ContentInfoDAO cid=new ContentInfoDAO();
//            boolean isContentInfo=cid.insert(match_name);
        //System.out.print(title+unit+content+addtime);
//        try {
//        	DBConn db=new DBConn();
//    		Connection con=db.getConn();
//    		Statement state=null;
//    		Statement state1=null;
//    		ResultSet rs=null;
//			state=con.createStatement();
//			String sql="insert into notyinfo(title,unit,content,addtime)values('"+title+"','"+unit+"','"+content+"','"+addtime+"')";
//			state.executeUpdate(sql);
//			state.close();
//			con.close();
//		} catch (SQLException e) {
//			bool=false;
//			// TODO Auto-generated catch block
//			e.printStackTrace();
//		}
        
            if(isMatchesInfo==true){
        //if(isNewsInfo==true){
            	String a = URLEncoder.encode("发布成功！", "UTF-8");  
        	    out.print("<script>alert(decodeURIComponent('"+a+"') );window.location.href='Match.jsp'</script>");
            }
            else{
        	    String a = URLEncoder.encode("未知错误！", "UTF-8");  
        	    out.print("<script>alert(decodeURIComponent('"+a+"') );history.back()</script>");
            }
        }
        else if(action.equals("delete")){
        	MatchesInfoDAO nid=new MatchesInfoDAO();
            boolean isMatchesInfo=nid.delete(id);
            if(isMatchesInfo==true){
                String a = URLEncoder.encode("删除成功！", "UTF-8");  
                out.print("<script>alert(decodeURIComponent('"+a+"') );window.location.href='Match.jsp'</script>");
            }
            else{
                String a = URLEncoder.encode("未知错误！", "UTF-8");  
                out.print("<script>alert(decodeURIComponent('"+a+"') );history.back()</script>");
                }
        }
        else if(action.equals("change")){
        	MatchesInfoDAO nid=new MatchesInfoDAO();
        	boolean isMatchesInfo=nid.update(id, match_name,introduction,start_time,end_time,rules,init_money);
        	if(isMatchesInfo==true){
        		String a = URLEncoder.encode("更改成功！", "UTF-8");  
                out.print("<script>alert(decodeURIComponent('"+a+"') );window.location.href='Match.jsp'</script>");
           	}
        	else{
                String a = URLEncoder.encode("未知错误！", "UTF-8");  
                out.print("<script>alert(decodeURIComponent('"+a+"') );history.back()</script>");        		
        	}
        }
	}
}
