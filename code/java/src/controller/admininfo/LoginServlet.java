package controller.admininfo;

import java.io.*;
import java.sql.Connection;
import java.sql.ResultSet;
import java.sql.SQLException;
import java.sql.Statement;

import javax.servlet.RequestDispatcher;
import javax.servlet.ServletException;
import javax.servlet.annotation.WebServlet;
import javax.servlet.http.HttpServlet;
import javax.servlet.http.HttpServletRequest;
import javax.servlet.http.HttpServletResponse;

import bean.admininfo.AdminInfo;
import bean.admininfo.AdminInfoDAO;
import utils.DBConn;


/**
 * Servlet implementation class LoginServlet
 */
@WebServlet(name = "LoginServlet1", urlPatterns = { "/LoginServlet1" })
public class LoginServlet extends HttpServlet {
private static final long serialVersionUID = 1L;

       
    /**
     * @see HttpServlet#HttpServlet()
     */
   /* public LoginServlet() {
        super();
        // TODO Auto-generated constructor stub
    }
*/
/**
* @see HttpServlet#doGet(HttpServletRequest request, HttpServletResponse response)
*/
protected void doGet(HttpServletRequest request, HttpServletResponse response) throws ServletException, IOException {
doPost(request, response);
}


/**
* @see HttpServlet#doPost(HttpServletRequest request, HttpServletResponse response)
*/
protected void doPost(HttpServletRequest request, HttpServletResponse response) throws ServletException, IOException {
// TODO Auto-generated method stub
//设置HTTP响应的文档类型,此处为Text/html,如果更改为application\msword则设置为word文档格式  
        response.setContentType("text/html");  
        //设置响应所采用的编码方式  
        response.setCharacterEncoding("utf-8");  
        AdminInfo user=new AdminInfo();
        String username=request.getParameter("username");
        String password=request.getParameter("password");
        user.setUsername(username);
        user.setPassword(password);
        boolean bool=false;
        PrintWriter out=response.getWriter();
        AdminInfoDAO aid=new AdminInfoDAO();
        bool=aid.checkAdmin(user);
		

        String forward;
        if(bool){					//验证成功后跳转
        	forward="Match.jsp";
        	RequestDispatcher rd=request.getRequestDispatcher(forward);
            rd.forward(request, response);
        }
        else{
        	out.flush();
        	out.println("<script>");
        	out.println("alert('账户或密码错误');");
        	out.println("history.back();");
        	out.println("</script>");
        }
	}
}