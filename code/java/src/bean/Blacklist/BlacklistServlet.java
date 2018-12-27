package bean.Blacklist;

import java.io.IOException;
import java.io.PrintWriter;
import java.net.URLEncoder;

import javax.servlet.RequestDispatcher;
import javax.servlet.ServletException;
import javax.servlet.http.HttpServlet;
import javax.servlet.http.HttpServletRequest;
import javax.servlet.http.HttpServletResponse;



import java.sql.*;
import java.text.ParseException;
import java.text.SimpleDateFormat;

import utils.DBConn;

/**
 * Servlet implementation class AddMatchesAction
 */
public class BlacklistServlet extends HttpServlet {
	private static final long serialVersionUID = 1L;
       
    /**
     * @see HttpServlet#HttpServlet()
     */
    public BlacklistServlet() {
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
		BlacklistInfo blacklist=new BlacklistInfo();
		response.setHeader("content-type", "text/html;charset=UTF-8");  
		response.setCharacterEncoding("UTF-8");  
		request.setCharacterEncoding("UTF-8"); 
		String wxid=request.getParameter("wxid");  	//接受post过来的变量
        String reason=request.getParameter("reason");  
        String id=request.getParameter("id");
        String op_time=request.getParameter("op_time");
        String action=request.getParameter("action");

        if(action.equals("insert")){				//根据传过来的action执行不同的操作
            BlacklistInfoDAO nid=new BlacklistInfoDAO();
            boolean isBlacklistInfo=nid.insert(wxid,reason);
            if(isBlacklistInfo==true){
            	String a = URLEncoder.encode("发布成功！", "UTF-8");  
        	    out.print("<script>alert(decodeURIComponent('"+a+"') );window.location.href='Blacklist.jsp'</script>");
            }
            else{
        	    String a = URLEncoder.encode("未知错误！", "UTF-8");  
        	    out.print("<script>alert(decodeURIComponent('"+a+"') );history.back()</script>");
            }
        }
        else if(action.equals("delete")){
        	BlacklistInfoDAO nid=new BlacklistInfoDAO();
            boolean isBlacklistInfo=nid.delete(id,wxid);
            if(isBlacklistInfo==true){
                String a = URLEncoder.encode("删除成功！", "UTF-8");  
                out.print("<script>alert(decodeURIComponent('"+a+"') );window.location.href='Blacklist.jsp'</script>");
            }
            else{
                String a = URLEncoder.encode("未知错误！", "UTF-8");  
                out.print("<script>alert(decodeURIComponent('"+a+"') );history.back()</script>");
                }
        }
	}
}
