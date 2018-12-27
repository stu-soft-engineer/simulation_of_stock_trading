package bean.Blacklist;

import java.io.IOException;
import java.io.PrintWriter;
import java.net.URLEncoder;
import java.text.*;
import java.sql.*;

import utils.DBConn;

public class BlacklistInfoDAO {
	public boolean insert(String wxid,String reason){
		try {
			SimpleDateFormat sdf = new SimpleDateFormat("yyyy-MM-dd HH:mm:ss"); 
        	DBConn db=new DBConn();				//同AdminInfoDAO
    		Connection con=db.getConn();
    		Statement state=null;
			state=con.createStatement();
			String type="黑名单";
			String detail1="“";
			String detail2="”被加入黑名单";
			long op_time = System.currentTimeMillis()/1000;

			String sql="insert into blacklist_db(wxid,reason,op_time)values('"+wxid+"','"+reason+"','"+op_time+"')";
			String sql1="insert into log_db(op_type,op_time,op_detail)values('"+type+"','"+op_time+"','"+detail1+wxid+detail2+"')";
			state.executeUpdate(sql);
			state.executeUpdate(sql1);
			state.close();
			con.close();
			return true;
		} catch (SQLException e) {
			// TODO Auto-generated catch block
			e.printStackTrace();
			
		}
		return false;
	}
	public boolean delete(String id,String wxid){
		try{
			DBConn db=new DBConn();
			Connection con=db.getConn();
			Statement state=null;
			state=con.createStatement();
			String type="黑名单";
			String detail1="“";
			String detail2="”被移出黑名单";
			long time = System.currentTimeMillis()/1000;
			
			String sql="delete from blacklist_db where id='"+id+"'";
			state.executeUpdate(sql);
			String sql1="insert into log_db(op_type,op_time,op_detail)values('"+type+"','"+time+"','"+detail1+wxid+detail2+"')";
			state.executeUpdate(sql1);
			state.close();
			con.close();
			return true;
		}catch(SQLException e){
			e.printStackTrace();
		}
		return false;
	}
}
