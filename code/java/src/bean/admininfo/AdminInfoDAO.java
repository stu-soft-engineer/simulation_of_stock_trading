package bean.admininfo;

import java.io.*;
import java.sql.Connection;
import java.sql.ResultSet;
import java.sql.SQLException;
import java.sql.Statement;

import bean.admininfo.AdminInfo;
import utils.DBConn;

public class AdminInfoDAO {
	public boolean checkAdmin(AdminInfo user){			//检查用户信息
		ResultSet rs=null;         
		Statement state=null;     
		try {
			DBConn db=new DBConn();							//连接数据库
			Connection conn=db.getConn();
			state=conn.createStatement();
			rs=state.executeQuery("select *from manager_db");	//用sql语句查询数据库
			while(rs.next()){
				if(user.getUsername().equals(rs.getString("account"))&&user.getPassword().equals(rs.getString("password"))){
					return true;
				}	
			}	
			conn.close();					//用完关闭
			state.close();
			rs.close();
		} catch (SQLException e) {
			// TODO Auto-generated catch block
			e.printStackTrace();
		} catch (Exception e) {
			// TODO Auto-generated catch block
			e.printStackTrace();
		}
		return false;
	}
	
//	public boolean registerAdmin(AdminInfo user){      				//注册账户  
//		Statement state=null;     
//		try {
//			DBConn db=new DBConn();
//			Connection conn=db.getConn();
//			state=conn.createStatement();
//			String sql="insert into admininfo values('"+user.getUsername()+"','"+user.getPassword()+"')";
//			state.executeUpdate(sql);
//			conn.close();
//			state.close();
//			return true;
//		} catch (SQLException e) {
//			// TODO Auto-generated catch block
//			e.printStackTrace();
//		} catch (Exception e) {
//			// TODO Auto-generated catch block
//			e.printStackTrace();
//		}
//		return false;
//	}
//	
//	
//	public boolean resetAdmin(AdminInfo user){        				//重置信息
//		Statement state=null;     
//		try {
//			DBConn db=new DBConn();
//			Connection conn=db.getConn();
//			state=conn.createStatement();
//			String sql="update admininfo set password='"+user.getPassword()+"' where username='"+user.getUsername()+"'";;
//			state.executeUpdate(sql);
//			conn.close();
//			state.close();
//			return true;
//		} catch (SQLException e) {
//			// TODO Auto-generated catch block
//			e.printStackTrace();
//		} catch (Exception e) {
//			// TODO Auto-generated catch block
//			e.printStackTrace();
//		}
//		return false;
//	}
}
