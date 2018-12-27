package bean.Blacklist;


public class BlacklistInfo {
	private int id;          //id号
	private String wxid;     //微信号
	private String reason;   //封号理由
	private String op_time;
	public int getId() {
		return id;
	}
	public void setId(int id) {
		this.id = id;
	}
	public String get_wxid() {
		return wxid;
	}
	public void set_wxid(String wxid) {
		this.wxid = wxid;
	}
	public String get_reason() {
		return reason;
	}
	public void set_reason(String reason) {
		this.reason = reason;
	}
	public String get_op_time() {
		return op_time;
	}
	public void set_op_time(String op_timen) {
		this.op_time = op_time;
	}

}
