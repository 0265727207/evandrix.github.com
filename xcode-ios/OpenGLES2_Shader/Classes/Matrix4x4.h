#ifndef st_Matrix4x4_h_
#define st_Matrix4x4_h_

struct Matrix4x4
{
	float m[16];
};


namespace Matrix4x4Utils
{
	void SetOrtho(Matrix4x4& m, float left, float right, float bottom, float top, float near, float far);
	void SetRotY(Matrix4x4& m, float angle);
	void SetRotZ(Matrix4x4& m, float angle);
	void Mul(Matrix4x4& m, const Matrix4x4& a, const Matrix4x4& b);
}


#endif
