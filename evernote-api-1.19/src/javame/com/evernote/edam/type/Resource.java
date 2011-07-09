/**
 * Autogenerated by Thrift
 *
 * DO NOT EDIT UNLESS YOU ARE SURE THAT YOU KNOW WHAT YOU ARE DOING
 */
package com.evernote.edam.type;

import java.util.Hashtable;
import java.util.Vector;
import java.util.Enumeration;

import org.apache.thrift.*;
import org.apache.thrift.meta_data.*;
import org.apache.thrift.transport.*;
import org.apache.thrift.protocol.*;

/**
 * Every media file that is embedded or attached to a note is represented
 * through a Resource entry.
 * <dl>
 * <dt>guid</dt>
 *   <dd>The unique identifier of this resource.  Will be set whenever
 *   a resource is retrieved from the service, but may be null when a client
 *   is creating a resource.
 *   <br/>
 *   Length:  EDAM_GUID_LEN_MIN - EDAM_GUID_LEN_MAX
 *   <br/>
 *   Regex:  EDAM_GUID_REGEX
 *   </dd>
 * 
 * <dt>noteGuid</dt>
 *   <dd>The unique identifier of the Note that holds this
 *   Resource. Will be set whenever the resource is retrieved from the service,
 *   but may be null when a client is creating a resource.
 *   <br/>
 *   Length:  EDAM_GUID_LEN_MIN - EDAM_GUID_LEN_MAX
 *   <br/>
 *   Regex:  EDAM_GUID_REGEX
 *   </dd>
 * 
 * <dt>data</dt>
 *   <dd>The contents of the resource.
 *   Maximum length:  The data.body is limited to EDAM_RESOURCE_SIZE_MAX_FREE
 *   for free accounts and EDAM_RESOURCE_SIZE_MAX_PREMIUM for premium accounts.
 *   </dd>
 * 
 * <dt>mime</dt>
 *   <dd>The MIME type for the embedded resource.  E.g. "image/gif"
 *   <br/>
 *   Length:  EDAM_MIME_LEN_MIN - EDAM_MIME_LEN_MAX
 *   <br/>
 *   Regex:  EDAM_MIME_REGEX
 *   </dd>
 * 
 * <dt>width</dt>
 *   <dd>If set, this contains the display width of this resource, in
 *   pixels.
 *   </dd>
 * 
 * <dt>height</dt>
 *   <dd>If set, this contains the display height of this resource,
 *   in pixels.
 *   </dd>
 * 
 * <dt>duration</dt>
 *   <dd>DEPRECATED: ignored.
 *   </dd>
 * 
 * <dt>active</dt>
 *   <dd>DEPRECATED: ignored.
 *   </dd>
 * 
 * <dt>recognition</dt>
 *   <dd>If set, this will hold the encoded data that provides
 *   information on search and recognition within this resource.
 *   </dd>
 * 
 * <dt>attributes</dt>
 *   <dd>A list of the attributes for this resource.
 *   </dd>
 * 
 * <dt>updateSequenceNum</dt>
 *   <dd>A number identifying the last transaction to
 *   modify the state of this object. The USN values are sequential within an
 *   account, and can be used to compare the order of modifications within the
 *   service.
 *   </dd>
 * 
 * <dt>alternateData</dt>
 *   <dd>Some Resources may be assigned an alternate data format by the service
 *   which may be more appropriate for indexing or rendering than the original
 *   data provided by the user.  In these cases, the alternate data form will
 *   be available via this Data element.  If a Resource has no alternate form,
 *   this field will be unset.</dd>
 * </dl>
 */
public class Resource implements TBase {
  private static final TStruct STRUCT_DESC = new TStruct("Resource");

  private static final TField GUID_FIELD_DESC = new TField("guid", TType.STRING, (short)1);
  private static final TField NOTE_GUID_FIELD_DESC = new TField("noteGuid", TType.STRING, (short)2);
  private static final TField DATA_FIELD_DESC = new TField("data", TType.STRUCT, (short)3);
  private static final TField MIME_FIELD_DESC = new TField("mime", TType.STRING, (short)4);
  private static final TField WIDTH_FIELD_DESC = new TField("width", TType.I16, (short)5);
  private static final TField HEIGHT_FIELD_DESC = new TField("height", TType.I16, (short)6);
  private static final TField DURATION_FIELD_DESC = new TField("duration", TType.I16, (short)7);
  private static final TField ACTIVE_FIELD_DESC = new TField("active", TType.BOOL, (short)8);
  private static final TField RECOGNITION_FIELD_DESC = new TField("recognition", TType.STRUCT, (short)9);
  private static final TField ATTRIBUTES_FIELD_DESC = new TField("attributes", TType.STRUCT, (short)11);
  private static final TField UPDATE_SEQUENCE_NUM_FIELD_DESC = new TField("updateSequenceNum", TType.I32, (short)12);
  private static final TField ALTERNATE_DATA_FIELD_DESC = new TField("alternateData", TType.STRUCT, (short)13);

  private String guid;
  private String noteGuid;
  private Data data;
  private String mime;
  private short width;
  private short height;
  private short duration;
  private boolean active;
  private Data recognition;
  private ResourceAttributes attributes;
  private int updateSequenceNum;
  private Data alternateData;

  // isset id assignments
  private static final int __WIDTH_ISSET_ID = 0;
  private static final int __HEIGHT_ISSET_ID = 1;
  private static final int __DURATION_ISSET_ID = 2;
  private static final int __ACTIVE_ISSET_ID = 3;
  private static final int __UPDATESEQUENCENUM_ISSET_ID = 4;
  private boolean[] __isset_vector = new boolean[5];

  public Resource() {
  }

  /**
   * Performs a deep copy on <i>other</i>.
   */
  public Resource(Resource other) {
    System.arraycopy(other.__isset_vector, 0, __isset_vector, 0, other.__isset_vector.length);
    if (other.isSetGuid()) {
      this.guid = other.guid;
    }
    if (other.isSetNoteGuid()) {
      this.noteGuid = other.noteGuid;
    }
    if (other.isSetData()) {
      this.data = new Data(other.data);
    }
    if (other.isSetMime()) {
      this.mime = other.mime;
    }
    this.width = other.width;
    this.height = other.height;
    this.duration = other.duration;
    this.active = other.active;
    if (other.isSetRecognition()) {
      this.recognition = new Data(other.recognition);
    }
    if (other.isSetAttributes()) {
      this.attributes = new ResourceAttributes(other.attributes);
    }
    this.updateSequenceNum = other.updateSequenceNum;
    if (other.isSetAlternateData()) {
      this.alternateData = new Data(other.alternateData);
    }
  }

  public Resource deepCopy() {
    return new Resource(this);
  }

  public Resource clone() {
    return new Resource(this);
  }

  public void clear() {
    this.guid = null;
    this.noteGuid = null;
    this.data = null;
    this.mime = null;
    setWidthIsSet(false);
    this.width = 0;
    setHeightIsSet(false);
    this.height = 0;
    setDurationIsSet(false);
    this.duration = 0;
    setActiveIsSet(false);
    this.active = false;
    this.recognition = null;
    this.attributes = null;
    setUpdateSequenceNumIsSet(false);
    this.updateSequenceNum = 0;
    this.alternateData = null;
  }

  public String getGuid() {
    return this.guid;
  }

  public void setGuid(String guid) {
    this.guid = guid;
  }

  public void unsetGuid() {
    this.guid = null;
  }

  /** Returns true if field guid is set (has been asigned a value) and false otherwise */
  public boolean isSetGuid() {
    return this.guid != null;
  }

  public void setGuidIsSet(boolean value) {
    if (!value) {
      this.guid = null;
    }
  }

  public String getNoteGuid() {
    return this.noteGuid;
  }

  public void setNoteGuid(String noteGuid) {
    this.noteGuid = noteGuid;
  }

  public void unsetNoteGuid() {
    this.noteGuid = null;
  }

  /** Returns true if field noteGuid is set (has been asigned a value) and false otherwise */
  public boolean isSetNoteGuid() {
    return this.noteGuid != null;
  }

  public void setNoteGuidIsSet(boolean value) {
    if (!value) {
      this.noteGuid = null;
    }
  }

  public Data getData() {
    return this.data;
  }

  public void setData(Data data) {
    this.data = data;
  }

  public void unsetData() {
    this.data = null;
  }

  /** Returns true if field data is set (has been asigned a value) and false otherwise */
  public boolean isSetData() {
    return this.data != null;
  }

  public void setDataIsSet(boolean value) {
    if (!value) {
      this.data = null;
    }
  }

  public String getMime() {
    return this.mime;
  }

  public void setMime(String mime) {
    this.mime = mime;
  }

  public void unsetMime() {
    this.mime = null;
  }

  /** Returns true if field mime is set (has been asigned a value) and false otherwise */
  public boolean isSetMime() {
    return this.mime != null;
  }

  public void setMimeIsSet(boolean value) {
    if (!value) {
      this.mime = null;
    }
  }

  public short getWidth() {
    return this.width;
  }

  public void setWidth(short width) {
    this.width = width;
    setWidthIsSet(true);
  }

  public void unsetWidth() {
    __isset_vector[__WIDTH_ISSET_ID] = false;
  }

  /** Returns true if field width is set (has been asigned a value) and false otherwise */
  public boolean isSetWidth() {
    return __isset_vector[__WIDTH_ISSET_ID];
  }

  public void setWidthIsSet(boolean value) {
    __isset_vector[__WIDTH_ISSET_ID] = value;
  }

  public short getHeight() {
    return this.height;
  }

  public void setHeight(short height) {
    this.height = height;
    setHeightIsSet(true);
  }

  public void unsetHeight() {
    __isset_vector[__HEIGHT_ISSET_ID] = false;
  }

  /** Returns true if field height is set (has been asigned a value) and false otherwise */
  public boolean isSetHeight() {
    return __isset_vector[__HEIGHT_ISSET_ID];
  }

  public void setHeightIsSet(boolean value) {
    __isset_vector[__HEIGHT_ISSET_ID] = value;
  }

  public short getDuration() {
    return this.duration;
  }

  public void setDuration(short duration) {
    this.duration = duration;
    setDurationIsSet(true);
  }

  public void unsetDuration() {
    __isset_vector[__DURATION_ISSET_ID] = false;
  }

  /** Returns true if field duration is set (has been asigned a value) and false otherwise */
  public boolean isSetDuration() {
    return __isset_vector[__DURATION_ISSET_ID];
  }

  public void setDurationIsSet(boolean value) {
    __isset_vector[__DURATION_ISSET_ID] = value;
  }

  public boolean isActive() {
    return this.active;
  }

  public void setActive(boolean active) {
    this.active = active;
    setActiveIsSet(true);
  }

  public void unsetActive() {
    __isset_vector[__ACTIVE_ISSET_ID] = false;
  }

  /** Returns true if field active is set (has been asigned a value) and false otherwise */
  public boolean isSetActive() {
    return __isset_vector[__ACTIVE_ISSET_ID];
  }

  public void setActiveIsSet(boolean value) {
    __isset_vector[__ACTIVE_ISSET_ID] = value;
  }

  public Data getRecognition() {
    return this.recognition;
  }

  public void setRecognition(Data recognition) {
    this.recognition = recognition;
  }

  public void unsetRecognition() {
    this.recognition = null;
  }

  /** Returns true if field recognition is set (has been asigned a value) and false otherwise */
  public boolean isSetRecognition() {
    return this.recognition != null;
  }

  public void setRecognitionIsSet(boolean value) {
    if (!value) {
      this.recognition = null;
    }
  }

  public ResourceAttributes getAttributes() {
    return this.attributes;
  }

  public void setAttributes(ResourceAttributes attributes) {
    this.attributes = attributes;
  }

  public void unsetAttributes() {
    this.attributes = null;
  }

  /** Returns true if field attributes is set (has been asigned a value) and false otherwise */
  public boolean isSetAttributes() {
    return this.attributes != null;
  }

  public void setAttributesIsSet(boolean value) {
    if (!value) {
      this.attributes = null;
    }
  }

  public int getUpdateSequenceNum() {
    return this.updateSequenceNum;
  }

  public void setUpdateSequenceNum(int updateSequenceNum) {
    this.updateSequenceNum = updateSequenceNum;
    setUpdateSequenceNumIsSet(true);
  }

  public void unsetUpdateSequenceNum() {
    __isset_vector[__UPDATESEQUENCENUM_ISSET_ID] = false;
  }

  /** Returns true if field updateSequenceNum is set (has been asigned a value) and false otherwise */
  public boolean isSetUpdateSequenceNum() {
    return __isset_vector[__UPDATESEQUENCENUM_ISSET_ID];
  }

  public void setUpdateSequenceNumIsSet(boolean value) {
    __isset_vector[__UPDATESEQUENCENUM_ISSET_ID] = value;
  }

  public Data getAlternateData() {
    return this.alternateData;
  }

  public void setAlternateData(Data alternateData) {
    this.alternateData = alternateData;
  }

  public void unsetAlternateData() {
    this.alternateData = null;
  }

  /** Returns true if field alternateData is set (has been asigned a value) and false otherwise */
  public boolean isSetAlternateData() {
    return this.alternateData != null;
  }

  public void setAlternateDataIsSet(boolean value) {
    if (!value) {
      this.alternateData = null;
    }
  }

  public boolean equals(Object that) {
    if (that == null)
      return false;
    if (that instanceof Resource)
      return this.equals((Resource)that);
    return false;
  }

  public boolean equals(Resource that) {
    if (that == null)
      return false;

    boolean this_present_guid = true && this.isSetGuid();
    boolean that_present_guid = true && that.isSetGuid();
    if (this_present_guid || that_present_guid) {
      if (!(this_present_guid && that_present_guid))
        return false;
      if (!this.guid.equals(that.guid))
        return false;
    }

    boolean this_present_noteGuid = true && this.isSetNoteGuid();
    boolean that_present_noteGuid = true && that.isSetNoteGuid();
    if (this_present_noteGuid || that_present_noteGuid) {
      if (!(this_present_noteGuid && that_present_noteGuid))
        return false;
      if (!this.noteGuid.equals(that.noteGuid))
        return false;
    }

    boolean this_present_data = true && this.isSetData();
    boolean that_present_data = true && that.isSetData();
    if (this_present_data || that_present_data) {
      if (!(this_present_data && that_present_data))
        return false;
      if (!this.data.equals(that.data))
        return false;
    }

    boolean this_present_mime = true && this.isSetMime();
    boolean that_present_mime = true && that.isSetMime();
    if (this_present_mime || that_present_mime) {
      if (!(this_present_mime && that_present_mime))
        return false;
      if (!this.mime.equals(that.mime))
        return false;
    }

    boolean this_present_width = true && this.isSetWidth();
    boolean that_present_width = true && that.isSetWidth();
    if (this_present_width || that_present_width) {
      if (!(this_present_width && that_present_width))
        return false;
      if (this.width != that.width)
        return false;
    }

    boolean this_present_height = true && this.isSetHeight();
    boolean that_present_height = true && that.isSetHeight();
    if (this_present_height || that_present_height) {
      if (!(this_present_height && that_present_height))
        return false;
      if (this.height != that.height)
        return false;
    }

    boolean this_present_duration = true && this.isSetDuration();
    boolean that_present_duration = true && that.isSetDuration();
    if (this_present_duration || that_present_duration) {
      if (!(this_present_duration && that_present_duration))
        return false;
      if (this.duration != that.duration)
        return false;
    }

    boolean this_present_active = true && this.isSetActive();
    boolean that_present_active = true && that.isSetActive();
    if (this_present_active || that_present_active) {
      if (!(this_present_active && that_present_active))
        return false;
      if (this.active != that.active)
        return false;
    }

    boolean this_present_recognition = true && this.isSetRecognition();
    boolean that_present_recognition = true && that.isSetRecognition();
    if (this_present_recognition || that_present_recognition) {
      if (!(this_present_recognition && that_present_recognition))
        return false;
      if (!this.recognition.equals(that.recognition))
        return false;
    }

    boolean this_present_attributes = true && this.isSetAttributes();
    boolean that_present_attributes = true && that.isSetAttributes();
    if (this_present_attributes || that_present_attributes) {
      if (!(this_present_attributes && that_present_attributes))
        return false;
      if (!this.attributes.equals(that.attributes))
        return false;
    }

    boolean this_present_updateSequenceNum = true && this.isSetUpdateSequenceNum();
    boolean that_present_updateSequenceNum = true && that.isSetUpdateSequenceNum();
    if (this_present_updateSequenceNum || that_present_updateSequenceNum) {
      if (!(this_present_updateSequenceNum && that_present_updateSequenceNum))
        return false;
      if (this.updateSequenceNum != that.updateSequenceNum)
        return false;
    }

    boolean this_present_alternateData = true && this.isSetAlternateData();
    boolean that_present_alternateData = true && that.isSetAlternateData();
    if (this_present_alternateData || that_present_alternateData) {
      if (!(this_present_alternateData && that_present_alternateData))
        return false;
      if (!this.alternateData.equals(that.alternateData))
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

    Resource other = (Resource)otherObject;    int lastComparison = 0;

    lastComparison = TBaseHelper.compareTo(isSetGuid(), other.isSetGuid());
    if (lastComparison != 0) {
      return lastComparison;
    }
    if (isSetGuid()) {
      lastComparison = TBaseHelper.compareTo(this.guid, other.guid);
      if (lastComparison != 0) {
        return lastComparison;
      }
    }
    lastComparison = TBaseHelper.compareTo(isSetNoteGuid(), other.isSetNoteGuid());
    if (lastComparison != 0) {
      return lastComparison;
    }
    if (isSetNoteGuid()) {
      lastComparison = TBaseHelper.compareTo(this.noteGuid, other.noteGuid);
      if (lastComparison != 0) {
        return lastComparison;
      }
    }
    lastComparison = TBaseHelper.compareTo(isSetData(), other.isSetData());
    if (lastComparison != 0) {
      return lastComparison;
    }
    if (isSetData()) {
      lastComparison = this.data.compareTo(other.data);
      if (lastComparison != 0) {
        return lastComparison;
      }
    }
    lastComparison = TBaseHelper.compareTo(isSetMime(), other.isSetMime());
    if (lastComparison != 0) {
      return lastComparison;
    }
    if (isSetMime()) {
      lastComparison = TBaseHelper.compareTo(this.mime, other.mime);
      if (lastComparison != 0) {
        return lastComparison;
      }
    }
    lastComparison = TBaseHelper.compareTo(isSetWidth(), other.isSetWidth());
    if (lastComparison != 0) {
      return lastComparison;
    }
    if (isSetWidth()) {
      lastComparison = TBaseHelper.compareTo(this.width, other.width);
      if (lastComparison != 0) {
        return lastComparison;
      }
    }
    lastComparison = TBaseHelper.compareTo(isSetHeight(), other.isSetHeight());
    if (lastComparison != 0) {
      return lastComparison;
    }
    if (isSetHeight()) {
      lastComparison = TBaseHelper.compareTo(this.height, other.height);
      if (lastComparison != 0) {
        return lastComparison;
      }
    }
    lastComparison = TBaseHelper.compareTo(isSetDuration(), other.isSetDuration());
    if (lastComparison != 0) {
      return lastComparison;
    }
    if (isSetDuration()) {
      lastComparison = TBaseHelper.compareTo(this.duration, other.duration);
      if (lastComparison != 0) {
        return lastComparison;
      }
    }
    lastComparison = TBaseHelper.compareTo(isSetActive(), other.isSetActive());
    if (lastComparison != 0) {
      return lastComparison;
    }
    if (isSetActive()) {
      lastComparison = TBaseHelper.compareTo(this.active, other.active);
      if (lastComparison != 0) {
        return lastComparison;
      }
    }
    lastComparison = TBaseHelper.compareTo(isSetRecognition(), other.isSetRecognition());
    if (lastComparison != 0) {
      return lastComparison;
    }
    if (isSetRecognition()) {
      lastComparison = this.recognition.compareTo(other.recognition);
      if (lastComparison != 0) {
        return lastComparison;
      }
    }
    lastComparison = TBaseHelper.compareTo(isSetAttributes(), other.isSetAttributes());
    if (lastComparison != 0) {
      return lastComparison;
    }
    if (isSetAttributes()) {
      lastComparison = this.attributes.compareTo(other.attributes);
      if (lastComparison != 0) {
        return lastComparison;
      }
    }
    lastComparison = TBaseHelper.compareTo(isSetUpdateSequenceNum(), other.isSetUpdateSequenceNum());
    if (lastComparison != 0) {
      return lastComparison;
    }
    if (isSetUpdateSequenceNum()) {
      lastComparison = TBaseHelper.compareTo(this.updateSequenceNum, other.updateSequenceNum);
      if (lastComparison != 0) {
        return lastComparison;
      }
    }
    lastComparison = TBaseHelper.compareTo(isSetAlternateData(), other.isSetAlternateData());
    if (lastComparison != 0) {
      return lastComparison;
    }
    if (isSetAlternateData()) {
      lastComparison = this.alternateData.compareTo(other.alternateData);
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
        case 1: // GUID
          if (field.type == TType.STRING) {
            this.guid = iprot.readString();
          } else { 
            TProtocolUtil.skip(iprot, field.type);
          }
          break;
        case 2: // NOTE_GUID
          if (field.type == TType.STRING) {
            this.noteGuid = iprot.readString();
          } else { 
            TProtocolUtil.skip(iprot, field.type);
          }
          break;
        case 3: // DATA
          if (field.type == TType.STRUCT) {
            this.data = new Data();
            this.data.read(iprot);
          } else { 
            TProtocolUtil.skip(iprot, field.type);
          }
          break;
        case 4: // MIME
          if (field.type == TType.STRING) {
            this.mime = iprot.readString();
          } else { 
            TProtocolUtil.skip(iprot, field.type);
          }
          break;
        case 5: // WIDTH
          if (field.type == TType.I16) {
            this.width = iprot.readI16();
            setWidthIsSet(true);
          } else { 
            TProtocolUtil.skip(iprot, field.type);
          }
          break;
        case 6: // HEIGHT
          if (field.type == TType.I16) {
            this.height = iprot.readI16();
            setHeightIsSet(true);
          } else { 
            TProtocolUtil.skip(iprot, field.type);
          }
          break;
        case 7: // DURATION
          if (field.type == TType.I16) {
            this.duration = iprot.readI16();
            setDurationIsSet(true);
          } else { 
            TProtocolUtil.skip(iprot, field.type);
          }
          break;
        case 8: // ACTIVE
          if (field.type == TType.BOOL) {
            this.active = iprot.readBool();
            setActiveIsSet(true);
          } else { 
            TProtocolUtil.skip(iprot, field.type);
          }
          break;
        case 9: // RECOGNITION
          if (field.type == TType.STRUCT) {
            this.recognition = new Data();
            this.recognition.read(iprot);
          } else { 
            TProtocolUtil.skip(iprot, field.type);
          }
          break;
        case 11: // ATTRIBUTES
          if (field.type == TType.STRUCT) {
            this.attributes = new ResourceAttributes();
            this.attributes.read(iprot);
          } else { 
            TProtocolUtil.skip(iprot, field.type);
          }
          break;
        case 12: // UPDATE_SEQUENCE_NUM
          if (field.type == TType.I32) {
            this.updateSequenceNum = iprot.readI32();
            setUpdateSequenceNumIsSet(true);
          } else { 
            TProtocolUtil.skip(iprot, field.type);
          }
          break;
        case 13: // ALTERNATE_DATA
          if (field.type == TType.STRUCT) {
            this.alternateData = new Data();
            this.alternateData.read(iprot);
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
    if (this.guid != null) {
      if (isSetGuid()) {
        oprot.writeFieldBegin(GUID_FIELD_DESC);
        oprot.writeString(this.guid);
        oprot.writeFieldEnd();
      }
    }
    if (this.noteGuid != null) {
      if (isSetNoteGuid()) {
        oprot.writeFieldBegin(NOTE_GUID_FIELD_DESC);
        oprot.writeString(this.noteGuid);
        oprot.writeFieldEnd();
      }
    }
    if (this.data != null) {
      if (isSetData()) {
        oprot.writeFieldBegin(DATA_FIELD_DESC);
        this.data.write(oprot);
        oprot.writeFieldEnd();
      }
    }
    if (this.mime != null) {
      if (isSetMime()) {
        oprot.writeFieldBegin(MIME_FIELD_DESC);
        oprot.writeString(this.mime);
        oprot.writeFieldEnd();
      }
    }
    if (isSetWidth()) {
      oprot.writeFieldBegin(WIDTH_FIELD_DESC);
      oprot.writeI16(this.width);
      oprot.writeFieldEnd();
    }
    if (isSetHeight()) {
      oprot.writeFieldBegin(HEIGHT_FIELD_DESC);
      oprot.writeI16(this.height);
      oprot.writeFieldEnd();
    }
    if (isSetDuration()) {
      oprot.writeFieldBegin(DURATION_FIELD_DESC);
      oprot.writeI16(this.duration);
      oprot.writeFieldEnd();
    }
    if (isSetActive()) {
      oprot.writeFieldBegin(ACTIVE_FIELD_DESC);
      oprot.writeBool(this.active);
      oprot.writeFieldEnd();
    }
    if (this.recognition != null) {
      if (isSetRecognition()) {
        oprot.writeFieldBegin(RECOGNITION_FIELD_DESC);
        this.recognition.write(oprot);
        oprot.writeFieldEnd();
      }
    }
    if (this.attributes != null) {
      if (isSetAttributes()) {
        oprot.writeFieldBegin(ATTRIBUTES_FIELD_DESC);
        this.attributes.write(oprot);
        oprot.writeFieldEnd();
      }
    }
    if (isSetUpdateSequenceNum()) {
      oprot.writeFieldBegin(UPDATE_SEQUENCE_NUM_FIELD_DESC);
      oprot.writeI32(this.updateSequenceNum);
      oprot.writeFieldEnd();
    }
    if (this.alternateData != null) {
      if (isSetAlternateData()) {
        oprot.writeFieldBegin(ALTERNATE_DATA_FIELD_DESC);
        this.alternateData.write(oprot);
        oprot.writeFieldEnd();
      }
    }
    oprot.writeFieldStop();
    oprot.writeStructEnd();
  }

  public String toString() {
    StringBuffer sb = new StringBuffer("Resource(");
    boolean first = true;

    if (isSetGuid()) {
      sb.append("guid:");
      if (this.guid == null) {
        sb.append("null");
      } else {
        sb.append(this.guid);
      }
      first = false;
    }
    if (isSetNoteGuid()) {
      if (!first) sb.append(", ");
      sb.append("noteGuid:");
      if (this.noteGuid == null) {
        sb.append("null");
      } else {
        sb.append(this.noteGuid);
      }
      first = false;
    }
    if (isSetData()) {
      if (!first) sb.append(", ");
      sb.append("data:");
      if (this.data == null) {
        sb.append("null");
      } else {
        sb.append(this.data);
      }
      first = false;
    }
    if (isSetMime()) {
      if (!first) sb.append(", ");
      sb.append("mime:");
      if (this.mime == null) {
        sb.append("null");
      } else {
        sb.append(this.mime);
      }
      first = false;
    }
    if (isSetWidth()) {
      if (!first) sb.append(", ");
      sb.append("width:");
      sb.append(this.width);
      first = false;
    }
    if (isSetHeight()) {
      if (!first) sb.append(", ");
      sb.append("height:");
      sb.append(this.height);
      first = false;
    }
    if (isSetDuration()) {
      if (!first) sb.append(", ");
      sb.append("duration:");
      sb.append(this.duration);
      first = false;
    }
    if (isSetActive()) {
      if (!first) sb.append(", ");
      sb.append("active:");
      sb.append(this.active);
      first = false;
    }
    if (isSetRecognition()) {
      if (!first) sb.append(", ");
      sb.append("recognition:");
      if (this.recognition == null) {
        sb.append("null");
      } else {
        sb.append(this.recognition);
      }
      first = false;
    }
    if (isSetAttributes()) {
      if (!first) sb.append(", ");
      sb.append("attributes:");
      if (this.attributes == null) {
        sb.append("null");
      } else {
        sb.append(this.attributes);
      }
      first = false;
    }
    if (isSetUpdateSequenceNum()) {
      if (!first) sb.append(", ");
      sb.append("updateSequenceNum:");
      sb.append(this.updateSequenceNum);
      first = false;
    }
    if (isSetAlternateData()) {
      if (!first) sb.append(", ");
      sb.append("alternateData:");
      if (this.alternateData == null) {
        sb.append("null");
      } else {
        sb.append(this.alternateData);
      }
      first = false;
    }
    sb.append(")");
    return sb.toString();
  }

  public void validate() throws TException {
    // check for required fields
  }

}

