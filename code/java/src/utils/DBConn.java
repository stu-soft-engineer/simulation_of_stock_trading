package utils;

import java.sql.Connection;
import java.sql.DriverManager;
import java.sql.ResultSet;
import java.sql.SQLException;
import java.sql.Statement;


public class DBConn {
public static String driver;//定义驱动
public static String url;//定义链接URL

public static String username;//定义数据库用户名
public static String password;//定义数据库密码
public static Connection connection;//定义链接
public static Statement statement;//定义statement
public static ResultSet result;//定义结果集

//设置connection
	{
		driver="com.mysql.jdbc.Driver";
//		url="jdbc:mysql://localhost:3306/oasystem";
//		username="root";
//		password="1234";     
		url="jdbc:mysql://119.23.36.18:3306/test_market";
		username="test_market";
		password="GrZFWfSh4GTMRBFy";  
		try {
			Class.forName(driver);
			connection=DriverManager.getConnection(url,username,password);
			System.out.println("链接成功--------------------------------");
		} catch (ClassNotFoundException e) {
			e.printStackTrace();
		}catch(SQLException ex){
			ex.printStackTrace();
		}
	}
 
    public DBConn(){     
        this.connection=this.getConn();  
    }     
  
    public Connection getConn(){     
        return this.connection;     
    } 
  
//    public void doInsert(String sql) {     
//     try {     
//    	 statement = connection.createStatement();     
//         int i = statement.executeUpdate(sql);     
//     } catch(SQLException sqlexception) {     
//         System.err.println("db.executeInset:" + sqlexception.getMessage());     
//     }finally{     
//              
//     }     
// }     
// 
// public void doDelete(String sql) {     
//     try {     
//    statement = connection.createStatement();     
//         int i = statement.executeUpdate(sql);     
//     } catch(SQLException sqlexception) {     
//         System.err.println("db.executeDelete:" + sqlexception.getMessage());     
//     }     
// }     
// public void doUpdate(String sql) {     
//     try {     
//    statement = connection.createStatement();     
//         int i = statement.executeUpdate(sql);     
//     } catch(SQLException sqlexception) {     
//         System.err.println("db.executeUpdate:" + sqlexception.getMessage());     
//     }     
// }     
//    
// public ResultSet doSelect(String sql) {     
//     try {  
//         connection=DriverManager.getConnection(url,username,password);  
//         statement = connection.createStatement(java.sql.ResultSet.TYPE_SCROLL_INSENSITIVE,java.sql.ResultSet.CONCUR_READ_ONLY);       
//         result = statement.executeQuery(sql);   
//         System.out.println("取得结果集");  
//     } catch(SQLException sqlexception) {     
//         System.err.println("db.executeQuery: " + sqlexception.getMessage());     
//     }     
//     return result;     
// }     
// /**   
//  *关闭数据库结果集，数据库操作对象，数据库链接
//    @Function: Close all the statement and conn int this instance and close the parameter ResultSet   
//    @Param: ResultSet   
//    @Exception: SQLException,Exception   
//   **/    
  public void close(ResultSet rs) throws SQLException, Exception {     
 
    if (rs != null) {     
      rs.close();     
      rs = null;     
    }     
 
    if (statement != null) {     
    statement.close();     
    statement = null;     
    }     
 
    if (connection != null) {     
    connection.close();     
    connection = null;     
    }     
  }     
 
  /**   
   *关闭数据库操作对象，数据库连接对象     
   * Close all the statement and conn int this instance   
   * @throws SQLException   
   * @throws Exception   
   */    
  public void close() throws SQLException, Exception {     
    if (statement != null) {     
    statement.close();     
    statement = null;     
    }     
 
    if (connection != null) {     
    connection.close();     
    connection = null;     
    }     
  }     
}