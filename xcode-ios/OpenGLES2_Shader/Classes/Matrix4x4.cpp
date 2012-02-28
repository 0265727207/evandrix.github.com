#include "Matrix4x4.h"
#include <math.h>


namespace Matrix4x4Utils
{

// http://www.opengl.org/sdk/docs/man/xhtml/glOrtho.xml
void SetOrtho(Matrix4x4& m, float left, float right, float bottom, float top, float near, float far)
{
	const float tx = - (right + left)/(right - left);
	const float ty = - (top + bottom)/(top - bottom);
	const float tz = - (far + near)/(far - near);

	m.m[0] = 2.0f/(right-left);
	m.m[1] = 0;
	m.m[2] = 0;
	m.m[3] = tx;
	
	m.m[4] = 0;
	m.m[5] = 2.0f/(top-bottom);
	m.m[6] = 0;
	m.m[7] = ty;
	
	m.m[8] = 0;
	m.m[9] = 0;
	m.m[10] = -2.0/(far-near);
	m.m[11] = tz;
	
	m.m[12] = 0;
	m.m[13] = 0;
	m.m[14] = 0;
	m.m[15] = 1;
}


void SetRotY(Matrix4x4& m, float angle)
{
	const float c = cosf(angle);
	const float s = sinf(angle);

	m.m[0] = c;
	m.m[1] = 0;
	m.m[2] = -s;
	m.m[3] = 0;

	m.m[4] = 0;
	m.m[5] = 1;
	m.m[6] = 0;
	m.m[7] = 0;

	m.m[8] = s;
	m.m[9] = 0;
	m.m[10] = c;
	m.m[11] = 0;
	
	m.m[12] = 0;
	m.m[13] = 0;
	m.m[14] = 0;
	m.m[15] = 1;	
}


void SetRotZ(Matrix4x4& m, float angle)
{
	const float c = cosf(angle);
	const float s = sinf(angle);

	m.m[0] = c;
	m.m[1] = -s;
	m.m[2] = 0;
	m.m[3] = 0;

	m.m[4] = s;
	m.m[5] = c;
	m.m[6] = 0;
	m.m[7] = 0;

	m.m[8] = 0;
	m.m[9] = 0;
	m.m[10] = 1;
	m.m[11] = 0;
	
	m.m[12] = 0;
	m.m[13] = 0;
	m.m[14] = 0;
	m.m[15] = 1;	
}


void Mul(Matrix4x4& m, const Matrix4x4& a, const Matrix4x4& b)
{
	m.m[0] = a.m[0]*b.m[0] + a.m[1]*b.m[4] + a.m[2]*b.m[8] + a.m[3]*b.m[12];
	m.m[1] = a.m[0]*b.m[1] + a.m[1]*b.m[5] + a.m[2]*b.m[9] + a.m[3]*b.m[13];
	m.m[2] = a.m[0]*b.m[2] + a.m[1]*b.m[6] + a.m[2]*b.m[10] + a.m[3]*b.m[14];
	m.m[3] = a.m[0]*b.m[3] + a.m[1]*b.m[7] + a.m[2]*b.m[11] + a.m[3]*b.m[15];

	m.m[4] = a.m[4]*b.m[0] + a.m[5]*b.m[4] + a.m[6]*b.m[8] + a.m[7]*b.m[12];
	m.m[5] = a.m[4]*b.m[1] + a.m[5]*b.m[5] + a.m[6]*b.m[9] + a.m[7]*b.m[13];
	m.m[6] = a.m[4]*b.m[2] + a.m[5]*b.m[6] + a.m[6]*b.m[10] + a.m[7]*b.m[14];
	m.m[7] = a.m[4]*b.m[3] + a.m[5]*b.m[7] + a.m[6]*b.m[11] + a.m[7]*b.m[15];

	m.m[8] = a.m[8]*b.m[0] + a.m[9]*b.m[4] + a.m[10]*b.m[8] + a.m[11]*b.m[12];
	m.m[9] = a.m[8]*b.m[1] + a.m[9]*b.m[5] + a.m[10]*b.m[9] + a.m[11]*b.m[13];
	m.m[10] = a.m[8]*b.m[2] + a.m[9]*b.m[6] + a.m[10]*b.m[10] + a.m[11]*b.m[14];
	m.m[11] = a.m[8]*b.m[3] + a.m[9]*b.m[7] + a.m[10]*b.m[11] + a.m[11]*b.m[15];

	m.m[12] = a.m[12]*b.m[0] + a.m[13]*b.m[4] + a.m[14]*b.m[8] + a.m[15]*b.m[12];
	m.m[13] = a.m[12]*b.m[1] + a.m[13]*b.m[5] + a.m[14]*b.m[9] + a.m[15]*b.m[13];
	m.m[14] = a.m[12]*b.m[2] + a.m[13]*b.m[6] + a.m[14]*b.m[10] + a.m[15]*b.m[14];
	m.m[15] = a.m[12]*b.m[3] + a.m[13]*b.m[7] + a.m[14]*b.m[11] + a.m[15]*b.m[15];
}


}
