package bean.matchesinfo;

import java.io.IOException;
import java.io.PrintWriter;
import java.net.URLEncoder;
import java.text.*;
import java.sql.*;

import utils.DBConn;

public class MatchesInfoDAO {
	public boolean insert(String match_name,String match_detail,String start_time_s,String end_time_s,String match_rule,String init_money){
		try {
			SimpleDateFormat sdf = new SimpleDateFormat("yyyy-MM-dd HH:mm:ss"); 
        	DBConn db=new DBConn();				//同AdminInfoDAO
    		Connection con=db.getConn();
    		Statement state=null;
			state=con.createStatement();
			String type="比赛";
			String detail1="增加“";
			String detail2="”比赛";
			long sign_timeLong = System.currentTimeMillis()/1000;
			int start_time=0,end_time=0;
			try {		//将字符串时间转换成时间戳
				start_time = Integer.parseInt(String.valueOf(sdf.parse(start_time_s).getTime()/1000));
				end_time=Integer.parseInt(String.valueOf(sdf.parse(end_time_s).getTime()/1000)); 
			} catch (NumberFormatException e) {
				// TODO Auto-generated catch block
				e.printStackTrace();
			} catch (ParseException e) {
				// TODO Auto-generated catch block
				e.printStackTrace();
			} 
			//int sign_time = new Long(sign_timeLong).intValue();
			String sql="insert into match_db(match_name,match_detail,start_time,sign_time,end_time,match_rule,init_money)values('"+match_name+"','"+match_detail+"','"+start_time+"','"+sign_timeLong+"','"+end_time+"','"+match_rule+"','"+init_money+"')";
			String sql1="insert into log_db(op_type,op_time,op_detail)values('"+type+"','"+sign_timeLong+"','"+detail1+match_name+detail2+"')";
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
			long time = System.currentTimeMillis()/1000;
			//int time = new Long(timeLong).intValue();			//操作的时间
			String sql="delete from match_db where id='"+id+"'";
			state.executeUpdate(sql);
			String sql1="insert into log_db(op_type,op_time,op_detail)values('"+type+"','"+time+"','"+detail1+match_name+detail2+"')";
			state.executeUpdate(sql1);
			state.close();
			con.close();
			return true;
		}catch(SQLException e){
			e.printStackTrace();
		}
		return false;
	}
	public boolean update(String id,String match_name,String match_detail,String start_time_s,String end_time_s,String match_rule,String init_money){
		try{
			SimpleDateFormat sdf = new SimpleDateFormat("yyyy-MM-dd HH:mm:ss"); 
		    DBConn db=new DBConn();
	    	Connection con=db.getConn();
		    Statement state=null;
		    state=con.createStatement();
//		    java.util.Date utilDate = new java.util.Date();
//            java.sql.Date addtime = new java.sql.Date(utilDate.getTime());
		    String type="比赛";
			String detail1="修改“";
			String detail2="”比赛";
			long time = System.currentTimeMillis()/1000;
						//操作的时间
			int start_time=0,end_time=0;
			try {		//将字符串时间转换成时间戳
				start_time = Integer.parseInt(String.valueOf(sdf.parse(start_time_s).getTime()/1000));
				end_time=Integer.parseInt(String.valueOf(sdf.parse(end_time_s).getTime()/1000)); 
			} catch (NumberFormatException e) {
				// TODO Auto-generated catch block
				e.printStackTrace();
			} catch (ParseException e) {
				// TODO Auto-generated catch block
				e.printStackTrace();
			}
			//String match_name_before="select match_name from match_db where id='"+id+"'";
            String sql="update match_db set match_name='"+match_name+"',match_detail='"+match_detail+"',start_time='"+start_time+"',end_time='"+end_time+"',match_rule='"+match_rule+"',init_money='"+init_money+"' where id='"+id+"'";
			String sql1="insert into log_db(op_type,op_time,op_detail)values('"+type+"','"+time+"','"+detail1+match_name+detail2+"')";
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
