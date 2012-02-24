// Compute a 32-bit hash function from a strings, using multilinear in 
// GF(2^32).
//
//
// apparently requires at least gcc 4.5 
// requires a processor with CLMUL support
//

#ifndef _CLMUL_H_
#define _CLMUL_H_
#include <wmmintrin.h>
#include <emmintrin.h>
#include <smmintrin.h>



// convenience function (not for speed!)
uint64 firstPart(__m128i x) {
	return _mm_cvtsi128_si64(x);
}

// convenience function (not for speed!)
uint64 secondPart(__m128i x) {
	return _mm_cvtsi128_si64(_mm_unpackhi_epi64(x,x));
}


///http://www.jjj.de/mathdata/minweight-primpoly.txt
const uint64 irredpoly = 1UL+(1UL<<2)+(1UL<<6)+(1UL<<7)+(1UL<<32);// it is important, for the algo. we have chosen that 7 is smaller equal than 16=32/2
const int n = 32;// degree of the polynomial

const uint64 mask = 0xFFFFFFFFUL;//32 bit mask for fast "% (1<<32)" computations
__m128i zerom128,C;// C is the irreducible poly.

// init must, obviously, be called first
void init_galois() {
	zerom128= _mm_setzero_si128();
	C = _mm_set_epi64x(0,irredpoly);// irred. poly with low value degrees
	printf("irred poly %llu %llu \n",firstPart(C), secondPart(C));

}

// convenience function
int is_zero(__m128i x) {
	return (_mm_movemask_epi8(_mm_cmpeq_epi32(x,zerom128)) == 0);
}
// convenience function
int equal(__m128i x,__m128i y) {
	return  is_zero(_mm_xor_si128 ( x,y));
}

/////////////////////////////////////////////////////////////////
// working from 
// "Modular Reduction in GF(2n) without Pre-computational Phase"
// by M. Knezevic, K. Sakiyama, J. Fan, and I. Verbauwhede (2008)
// algo. 4
//
// A is input, M is irred. (n=32)
//
//(((A div x^n) * M ) div x^n) * M) mod x^n
//+(A mod x^n)
//////////////////////////////////////////////////
uint32 barrettWithoutPrecomputation( __m128i A) {
	/////////////////
	/// This algo. requires two multiplications (_mm_clmulepi64_si128)
	/// They are probably the bottleneck.
	/// Note: Barrett's original algorithm also required two multiplications.
	////////////////
	__m128i Q1 = _mm_srli_epi64 (A, n);
	__m128i Q2 = _mm_clmulepi64_si128( Q1, C, 0x00);// A div x^n
	__m128i Q3 = _mm_srli_epi64 (Q2, n);
	// commenting out the long way derived from the paper (following two lines are enough)
	//__m128i R1 = _mm_and_si128 (maskm128,A);
	//__m128i R2 = _mm_and_si128 (maskm128,_mm_clmulepi64_si128( Q3, C, 0x00));
	//__m128i final  = _mm_xor_si128 (R1, R2);
	__m128i final  = _mm_xor_si128 (A, _mm_clmulepi64_si128( Q3, C, 0x00));		
	return _mm_cvtsi128_si64(final);// & mask;
 
}


// make sure to call init before you can this function!
uint64 hashGaloisFieldMultilinear(const uint64 *  randomsource, const uint32 *  string, const uint32 * const endstring) {
	 const uint32 *  randomsource32 = ( const uint32 * )randomsource;
    __m128i acc = _mm_set_epi64x(0,*(randomsource32++));
    for(; string!= endstring; ++randomsource32,++string ) {
    	__m128i temp = _mm_set_epi64x(*randomsource32,*string);
    	__m128i clprod  = _mm_clmulepi64_si128( temp, temp, 0x10);
        acc = _mm_xor_si128 (clprod,acc);   
    }
    return barrettWithoutPrecomputation(acc);
}

// make sure to call init before you can this function!
uint64 hashGaloisFieldMultilinearHalfMultiplications(const uint64 *  randomsource, const uint32 *  string, const uint32 * const endstring) {
	const uint32 *  randomsource32 = ( const uint32 * )randomsource;
    __m128i acc = _mm_set_epi64x(0,*(randomsource32++));
    for(; string!= endstring; randomsource32+=2,string+=2 ) {
    	// could find a way to replace this with _mm_load_si128, but it is not obvious how
    	__m128i temp1 = _mm_set_epi64x(*randomsource32,*(randomsource32+1));
    	__m128i temp2 = _mm_set_epi64x(*string,*(string+1));
    	__m128i twosums = _mm_xor_si128(temp1,temp2); 
    	__m128i clprod  = _mm_clmulepi64_si128( twosums, twosums, 0x10);
        acc = _mm_xor_si128 (clprod,acc);   
    }
    return barrettWithoutPrecomputation(acc);
}

#endif