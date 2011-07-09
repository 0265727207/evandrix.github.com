/**
 * Autogenerated by Thrift
 *
 * DO NOT EDIT UNLESS YOU ARE SURE THAT YOU KNOW WHAT YOU ARE DOING
 */
using System;
using System.Collections;
using System.Collections.Generic;
using System.Text;
using System.IO;
using Thrift;
using Thrift.Collections;
using Thrift.Protocol;
using Thrift.Transport;
namespace Evernote.EDAM.UserStore
{

  [Serializable]
  public partial class PublicUserInfo : TBase
  {
    private int userId;
    private string shardId;
    private Evernote.EDAM.Type.PrivilegeLevel privilege;
    private string username;

    public int UserId
    {
      get
      {
        return userId;
      }
      set
      {
        __isset.userId = true;
        this.userId = value;
      }
    }

    public string ShardId
    {
      get
      {
        return shardId;
      }
      set
      {
        __isset.shardId = true;
        this.shardId = value;
      }
    }

    public Evernote.EDAM.Type.PrivilegeLevel Privilege
    {
      get
      {
        return privilege;
      }
      set
      {
        __isset.privilege = true;
        this.privilege = value;
      }
    }

    public string Username
    {
      get
      {
        return username;
      }
      set
      {
        __isset.username = true;
        this.username = value;
      }
    }


    public Isset __isset;
    [Serializable]
    public struct Isset {
      public bool userId;
      public bool shardId;
      public bool privilege;
      public bool username;
    }

    public PublicUserInfo() {
    }

    public void Read (TProtocol iprot)
    {
      TField field;
      iprot.ReadStructBegin();
      while (true)
      {
        field = iprot.ReadFieldBegin();
        if (field.Type == TType.Stop) { 
          break;
        }
        switch (field.ID)
        {
          case 1:
            if (field.Type == TType.I32) {
              this.userId = iprot.ReadI32();
              this.__isset.userId = true;
            } else { 
              TProtocolUtil.Skip(iprot, field.Type);
            }
            break;
          case 2:
            if (field.Type == TType.String) {
              this.shardId = iprot.ReadString();
              this.__isset.shardId = true;
            } else { 
              TProtocolUtil.Skip(iprot, field.Type);
            }
            break;
          case 3:
            if (field.Type == TType.I32) {
              this.privilege = (Evernote.EDAM.Type.PrivilegeLevel)iprot.ReadI32();
              this.__isset.privilege = true;
            } else { 
              TProtocolUtil.Skip(iprot, field.Type);
            }
            break;
          case 4:
            if (field.Type == TType.String) {
              this.username = iprot.ReadString();
              this.__isset.username = true;
            } else { 
              TProtocolUtil.Skip(iprot, field.Type);
            }
            break;
          default: 
            TProtocolUtil.Skip(iprot, field.Type);
            break;
        }
        iprot.ReadFieldEnd();
      }
      iprot.ReadStructEnd();
    }

    public void Write(TProtocol oprot) {
      TStruct struc = new TStruct("PublicUserInfo");
      oprot.WriteStructBegin(struc);
      TField field = new TField();
      if (__isset.userId) {
        field.Name = "userId";
        field.Type = TType.I32;
        field.ID = 1;
        oprot.WriteFieldBegin(field);
        oprot.WriteI32(this.userId);
        oprot.WriteFieldEnd();
      }
      if (this.shardId != null && __isset.shardId) {
        field.Name = "shardId";
        field.Type = TType.String;
        field.ID = 2;
        oprot.WriteFieldBegin(field);
        oprot.WriteString(this.shardId);
        oprot.WriteFieldEnd();
      }
      if (__isset.privilege) {
        field.Name = "privilege";
        field.Type = TType.I32;
        field.ID = 3;
        oprot.WriteFieldBegin(field);
        oprot.WriteI32((int)this.privilege);
        oprot.WriteFieldEnd();
      }
      if (this.username != null && __isset.username) {
        field.Name = "username";
        field.Type = TType.String;
        field.ID = 4;
        oprot.WriteFieldBegin(field);
        oprot.WriteString(this.username);
        oprot.WriteFieldEnd();
      }
      oprot.WriteFieldStop();
      oprot.WriteStructEnd();
    }

    public override string ToString() {
      StringBuilder sb = new StringBuilder("PublicUserInfo(");
      sb.Append("userId: ");
      sb.Append(this.userId);
      sb.Append(",shardId: ");
      sb.Append(this.shardId);
      sb.Append(",privilege: ");
      sb.Append(this.privilege);
      sb.Append(",username: ");
      sb.Append(this.username);
      sb.Append(")");
      return sb.ToString();
    }

  }

}
