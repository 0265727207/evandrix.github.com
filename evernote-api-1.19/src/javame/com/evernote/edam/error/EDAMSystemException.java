/**
 * Autogenerated by Thrift
 *
 * DO NOT EDIT UNLESS YOU ARE SURE THAT YOU KNOW WHAT YOU ARE DOING
 */
package com.evernote.edam.error;

import java.util.Hashtable;
import java.util.Vector;
import java.util.Enumeration;

import org.apache.thrift.*;
import org.apache.thrift.meta_data.*;
import org.apache.thrift.transport.*;
import org.apache.thrift.protocol.*;

/**
 * This exception is thrown by EDAM procedures when a call fails as a result of
 * an a problem in the service that could not be changed through user action.
 * 
 * errorCode:  The numeric code indicating the type of error that occurred.
 *   must be one of the values of EDAMErrorCode.
 * 
 * message:  This may contain additional information about the error
 */
public class EDAMSystemException extends Exception implements TBase {
  private static final TStruct STRUCT_DESC = new TStruct("EDAMSystemException");

  private static final TField ERROR_CODE_FIELD_DESC = new TField("errorCode", TType.I32, (short)1);
  private static final TField MESSAGE_FIELD_DESC = new TField("message", TType.STRING, (short)2);

  private EDAMErrorCode errorCode;
  private String message;

  // isset id assignments

  public EDAMSystemException() {
  }

  public EDAMSystemException(
    EDAMErrorCode errorCode)
  {
    this();
    this.errorCode = errorCode;
  }

  /**
   * Performs a deep copy on <i>other</i>.
   */
  public EDAMSystemException(EDAMSystemException other) {
    if (other.isSetErrorCode()) {
      this.errorCode = other.errorCode;
    }
    if (other.isSetMessage()) {
      this.message = other.message;
    }
  }

  public EDAMSystemException deepCopy() {
    return new EDAMSystemException(this);
  }

  public EDAMSystemException clone() {
    return new EDAMSystemException(this);
  }

  public void clear() {
    this.errorCode = null;
    this.message = null;
  }

  /**
   * 
   * @see EDAMErrorCode
   */
  public EDAMErrorCode getErrorCode() {
    return this.errorCode;
  }

  /**
   * 
   * @see EDAMErrorCode
   */
  public void setErrorCode(EDAMErrorCode errorCode) {
    this.errorCode = errorCode;
  }

  public void unsetErrorCode() {
    this.errorCode = null;
  }

  /** Returns true if field errorCode is set (has been asigned a value) and false otherwise */
  public boolean isSetErrorCode() {
    return this.errorCode != null;
  }

  public void setErrorCodeIsSet(boolean value) {
    if (!value) {
      this.errorCode = null;
    }
  }

  public String getMessage() {
    return this.message;
  }

  public void setMessage(String message) {
    this.message = message;
  }

  public void unsetMessage() {
    this.message = null;
  }

  /** Returns true if field message is set (has been asigned a value) and false otherwise */
  public boolean isSetMessage() {
    return this.message != null;
  }

  public void setMessageIsSet(boolean value) {
    if (!value) {
      this.message = null;
    }
  }

  public boolean equals(Object that) {
    if (that == null)
      return false;
    if (that instanceof EDAMSystemException)
      return this.equals((EDAMSystemException)that);
    return false;
  }

  public boolean equals(EDAMSystemException that) {
    if (that == null)
      return false;

    boolean this_present_errorCode = true && this.isSetErrorCode();
    boolean that_present_errorCode = true && that.isSetErrorCode();
    if (this_present_errorCode || that_present_errorCode) {
      if (!(this_present_errorCode && that_present_errorCode))
        return false;
      if (!this.errorCode.equals(that.errorCode))
        return false;
    }

    boolean this_present_message = true && this.isSetMessage();
    boolean that_present_message = true && that.isSetMessage();
    if (this_present_message || that_present_message) {
      if (!(this_present_message && that_present_message))
        return false;
      if (!this.message.equals(that.message))
        return false;
    }

    return true;
  }

  public int hashCode() {
    return 0;
  }

  public int compareTo(Object otherObject) {
    if (!getClass().equals(otherObject.getClass())) {
      return getClass().getName().compareTo(otherObject.getClass().getName());
    }

    EDAMSystemException other = (EDAMSystemException)otherObject;    int lastComparison = 0;

    lastComparison = TBaseHelper.compareTo(isSetErrorCode(), other.isSetErrorCode());
    if (lastComparison != 0) {
      return lastComparison;
    }
    if (isSetErrorCode()) {
      lastComparison = TBaseHelper.compareTo(this.errorCode, other.errorCode);
      if (lastComparison != 0) {
        return lastComparison;
      }
    }
    lastComparison = TBaseHelper.compareTo(isSetMessage(), other.isSetMessage());
    if (lastComparison != 0) {
      return lastComparison;
    }
    if (isSetMessage()) {
      lastComparison = TBaseHelper.compareTo(this.message, other.message);
      if (lastComparison != 0) {
        return lastComparison;
      }
    }
    return 0;
  }

  public void read(TProtocol iprot) throws TException {
    TField field;
    iprot.readStructBegin();
    while (true)
    {
      field = iprot.readFieldBegin();
      if (field.type == TType.STOP) { 
        break;
      }
      switch (field.id) {
        case 1: // ERROR_CODE
          if (field.type == TType.I32) {
            this.errorCode = EDAMErrorCode.findByValue(iprot.readI32());
          } else { 
            TProtocolUtil.skip(iprot, field.type);
          }
          break;
        case 2: // MESSAGE
          if (field.type == TType.STRING) {
            this.message = iprot.readString();
          } else { 
            TProtocolUtil.skip(iprot, field.type);
          }
          break;
        default:
          TProtocolUtil.skip(iprot, field.type);
      }
      iprot.readFieldEnd();
    }
    iprot.readStructEnd();
    validate();
  }

  public void write(TProtocol oprot) throws TException {
    validate();

    oprot.writeStructBegin(STRUCT_DESC);
    if (this.errorCode != null) {
      oprot.writeFieldBegin(ERROR_CODE_FIELD_DESC);
      oprot.writeI32(this.errorCode.getValue());
      oprot.writeFieldEnd();
    }
    if (this.message != null) {
      if (isSetMessage()) {
        oprot.writeFieldBegin(MESSAGE_FIELD_DESC);
        oprot.writeString(this.message);
        oprot.writeFieldEnd();
      }
    }
    oprot.writeFieldStop();
    oprot.writeStructEnd();
  }

  public String toString() {
    StringBuffer sb = new StringBuffer("EDAMSystemException(");
    boolean first = true;

    sb.append("errorCode:");
    if (this.errorCode == null) {
      sb.append("null");
    } else {
      sb.append(this.errorCode);
    }
    first = false;
    if (isSetMessage()) {
      if (!first) sb.append(", ");
      sb.append("message:");
      if (this.message == null) {
        sb.append("null");
      } else {
        sb.append(this.message);
      }
      first = false;
    }
    sb.append(")");
    return sb.toString();
  }

  public void validate() throws TException {
    // check for required fields
    if (!isSetErrorCode()) {
      throw new TProtocolException("Required field 'errorCode' is unset! Struct:" + toString());
    }

  }

}

