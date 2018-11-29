package bean.admininfo;

import java.io.*;
import java.sql.Connection;
import java.sql.ResultSet;
import java.sql.SQLException;
import java.sql.Statement;

import bean.admininfo.AdminInfo;
import utils.DBConn;

public class AdminInfoDAO {
	public boolean checkAdmin(AdminInfo user){
		ResultSet rs=null;         
		Statement state=null;     
		try {
			DBConn db=new DBConn();
			Connection conn=db.getConn();
			state=conn.createStatement();
			rs=state.executeQuery("select *from manager_db");
			while(rs.next()){
				if(user.getUsername().equals(rs.getString("account"))&&user.getPassword().equals(rs.getString("password"))){
					return true;
				}	
			}	
			conn.close();
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
	
//	public boolean superCheckAdmin(AdminInfo user){
//		ResultSet rs=null;         
//		Statement state=null;     
//		try {
//			DBConn db=new DBConn();
//			Connection conn=db.getConn();
//			state=conn.createStatement();
//			rs=state.executeQuery("select *from admininfo");
//			while(rs.next()){
//				if(user.getUsername().equals(rs.getString("username"))){
//					return true;
//				}	
//			}	
//			conn.close();
//			state.close();
//			rs.close();
//		} catch (SQLException e) {
//			// TODO Auto-generated catch block
//			e.printStackTrace();
//		} catch (Exception e) {
//			// TODO Auto-generated catch block
//			e.printStackTrace();
//		}
//		return false;
//	}
	
	public boolean registerAdmin(AdminInfo user){        
		Statement state=null;     
		try {
			DBConn db=new DBConn();
			Connection conn=db.getConn();
			state=conn.createStatement();
			String sql="insert into admininfo values('"+user.getUsername()+"','"+user.getPassword()+"')";
			state.executeUpdate(sql);
			conn.close();
			state.close();
			return true;
		} catch (SQLException e) {
			// TODO Auto-generated catch block
			e.printStackTrace();
		} catch (Exception e) {
			// TODO Auto-generated catch block
			e.printStackTrace();
		}
		return false;
	}
	
	
	public boolean resetAdmin(AdminInfo user){        
		Statement state=null;     
		try {
			DBConn db=new DBConn();
			Connection conn=db.getConn();
			state=conn.createStatement();
			String sql="update admininfo set password='"+user.getPassword()+"' where username='"+user.getUsername()+"'";;
			state.executeUpdate(sql);
			conn.close();
			state.close();
			return true;
		} catch (SQLException e) {
			// TODO Auto-generated catch block
			e.printStackTrace();
		} catch (Exception e) {
			// TODO Auto-generated catch block
			e.printStackTrace();
		}
		return false;
	}
}
