package bean.matchesinfo;

import java.io.IOException;
import java.io.PrintWriter;
import java.net.URLEncoder;


import java.sql.*;
import java.text.SimpleDateFormat;

import utils.DBConn;

public class MatchesInfoDAO {
	public boolean insert(String match_name,String introduction,String start_time,String end_time,String rules,String init_money){
		try {
        	DBConn db=new DBConn();				//同AdminInfoDAO
    		Connection con=db.getConn();
    		Statement state=null;
			state=con.createStatement();
			String type="比赛";
			String detail1="增加“";
			String detail2="”比赛";
			//java.util.Date utilDate = new java.util.Date();
	        //java.sql.Date regist_time = new java.sql.Date(utilDate.getTime());
			String sql="insert into match_db(match_name,introduction,start_time,end_time,rules,init_money)values('"+match_name+"','"+introduction+"','"+start_time+"','"+end_time+"','"+rules+"','"+init_money+"')";
			String sql1="insert into log_db(op_type,op_detail)values('"+type+"','"+detail1+match_name+detail2+"')";
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
	public boolean delete(String id,String match_name){
		try{
			DBConn db=new DBConn();
			Connection con=db.getConn();
			Statement state=null;
			state=con.createStatement();
			String type="比赛";
			String detail1="删除“";
			String detail2="”比赛";
			System.out.println("id:"+id);
			String sql="delete from match_db where id='"+id+"'";
			state.executeUpdate(sql);
			String sql1="insert into log_db(op_type,op_detail)values('"+type+"','"+detail1+match_name+detail2+"')";
			state.executeUpdate(sql1);
			state.close();
			con.close();
			return true;
		}catch(SQLException e){
			e.printStackTrace();
		}
		return false;
	}
	public boolean update(String id,String match_name,String introduction,String start_time,String end_time,String rules,String init_money){
		try{
		    DBConn db=new DBConn();
	    	Connection con=db.getConn();
		    Statement state=null;
		    state=con.createStatement();
//		    java.util.Date utilDate = new java.util.Date();
//            java.sql.Date addtime = new java.sql.Date(utilDate.getTime());
		    String type="比赛";
			String detail1="修改“";
			String detail2="”比赛";

			//String match_name_before="select match_name from match_db where id='"+id+"'";
            String sql="update match_db set match_name='"+match_name+"',introduction='"+introduction+"',start_time='"+start_time+"',end_time='"+end_time+"',rules='"+rules+"',init_money='"+init_money+"' where id='"+id+"'";
			String sql1="insert into log_db(op_type,op_detail)values('"+type+"','"+detail1+match_name+detail2+"')";
            state.executeUpdate(sql);
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
