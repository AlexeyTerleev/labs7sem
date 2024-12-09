// IL code: compiled_code
.class private auto ansi '<Module>'
{
} // end of class <Module>

.class private auto ansi sealed beforefieldinit Microsoft.CodeAnalysis.EmbeddedAttribute
	extends [System.Runtime]System.Attribute
{
	.custom instance void [System.Runtime]System.Runtime.CompilerServices.CompilerGeneratedAttribute::.ctor() = (
		01 00 00 00
	)
	.custom instance void Microsoft.CodeAnalysis.EmbeddedAttribute::.ctor() = (
		01 00 00 00
	)
	// Methods
	.method public hidebysig specialname rtspecialname 
		instance void .ctor () cil managed 
	{
		// Method begins at RVA 0x2050
		// Header size: 1
		// Code size: 8 (0x8)
		.maxstack 8

		IL_0000: ldarg.0
		IL_0001: call instance void [System.Runtime]System.Attribute::.ctor()
		IL_0006: nop
		IL_0007: ret
	} // end of method EmbeddedAttribute::.ctor

} // end of class Microsoft.CodeAnalysis.EmbeddedAttribute

.class private auto ansi sealed beforefieldinit System.Runtime.CompilerServices.NullableAttribute
	extends [System.Runtime]System.Attribute
{
	.custom instance void [System.Runtime]System.Runtime.CompilerServices.CompilerGeneratedAttribute::.ctor() = (
		01 00 00 00
	)
	.custom instance void Microsoft.CodeAnalysis.EmbeddedAttribute::.ctor() = (
		01 00 00 00
	)
	.custom instance void [System.Runtime]System.AttributeUsageAttribute::.ctor(valuetype [System.Runtime]System.AttributeTargets) = (
		01 00 84 6b 00 00 02 00 54 02 0d 41 6c 6c 6f 77
		4d 75 6c 74 69 70 6c 65 00 54 02 09 49 6e 68 65
		72 69 74 65 64 00
	)
	// Fields
	.field public initonly uint8[] NullableFlags

	// Methods
	.method public hidebysig specialname rtspecialname 
		instance void .ctor (
			uint8 ''
		) cil managed 
	{
		// Method begins at RVA 0x2059
		// Header size: 1
		// Code size: 24 (0x18)
		.maxstack 8

		IL_0000: ldarg.0
		IL_0001: call instance void [System.Runtime]System.Attribute::.ctor()
		IL_0006: nop
		IL_0007: ldarg.0
		IL_0008: ldc.i4.1
		IL_0009: newarr [System.Runtime]System.Byte
		IL_000e: dup
		IL_000f: ldc.i4.0
		IL_0010: ldarg.1
		IL_0011: stelem.i1
		IL_0012: stfld uint8[] System.Runtime.CompilerServices.NullableAttribute::NullableFlags
		IL_0017: ret
	} // end of method NullableAttribute::.ctor

	.method public hidebysig specialname rtspecialname 
		instance void .ctor (
			uint8[] ''
		) cil managed 
	{
		// Method begins at RVA 0x2072
		// Header size: 1
		// Code size: 15 (0xf)
		.maxstack 8

		IL_0000: ldarg.0
		IL_0001: call instance void [System.Runtime]System.Attribute::.ctor()
		IL_0006: nop
		IL_0007: ldarg.0
		IL_0008: ldarg.1
		IL_0009: stfld uint8[] System.Runtime.CompilerServices.NullableAttribute::NullableFlags
		IL_000e: ret
	} // end of method NullableAttribute::.ctor

} // end of class System.Runtime.CompilerServices.NullableAttribute

.class private auto ansi sealed beforefieldinit System.Runtime.CompilerServices.NullableContextAttribute
	extends [System.Runtime]System.Attribute
{
	.custom instance void [System.Runtime]System.Runtime.CompilerServices.CompilerGeneratedAttribute::.ctor() = (
		01 00 00 00
	)
	.custom instance void Microsoft.CodeAnalysis.EmbeddedAttribute::.ctor() = (
		01 00 00 00
	)
	.custom instance void [System.Runtime]System.AttributeUsageAttribute::.ctor(valuetype [System.Runtime]System.AttributeTargets) = (
		01 00 4c 14 00 00 02 00 54 02 0d 41 6c 6c 6f 77
		4d 75 6c 74 69 70 6c 65 00 54 02 09 49 6e 68 65
		72 69 74 65 64 00
	)
	// Fields
	.field public initonly uint8 Flag

	// Methods
	.method public hidebysig specialname rtspecialname 
		instance void .ctor (
			uint8 ''
		) cil managed 
	{
		// Method begins at RVA 0x2082
		// Header size: 1
		// Code size: 15 (0xf)
		.maxstack 8

		IL_0000: ldarg.0
		IL_0001: call instance void [System.Runtime]System.Attribute::.ctor()
		IL_0006: nop
		IL_0007: ldarg.0
		IL_0008: ldarg.1
		IL_0009: stfld uint8 System.Runtime.CompilerServices.NullableContextAttribute::Flag
		IL_000e: ret
	} // end of method NullableContextAttribute::.ctor

} // end of class System.Runtime.CompilerServices.NullableContextAttribute

.class private auto ansi sealed beforefieldinit System.Runtime.CompilerServices.RefSafetyRulesAttribute
	extends [System.Runtime]System.Attribute
{
	.custom instance void [System.Runtime]System.Runtime.CompilerServices.CompilerGeneratedAttribute::.ctor() = (
		01 00 00 00
	)
	.custom instance void Microsoft.CodeAnalysis.EmbeddedAttribute::.ctor() = (
		01 00 00 00
	)
	.custom instance void [System.Runtime]System.AttributeUsageAttribute::.ctor(valuetype [System.Runtime]System.AttributeTargets) = (
		01 00 02 00 00 00 02 00 54 02 0d 41 6c 6c 6f 77
		4d 75 6c 74 69 70 6c 65 00 54 02 09 49 6e 68 65
		72 69 74 65 64 00
	)
	// Fields
	.field public initonly int32 Version

	// Methods
	.method public hidebysig specialname rtspecialname 
		instance void .ctor (
			int32 ''
		) cil managed 
	{
		// Method begins at RVA 0x2092
		// Header size: 1
		// Code size: 15 (0xf)
		.maxstack 8

		IL_0000: ldarg.0
		IL_0001: call instance void [System.Runtime]System.Attribute::.ctor()
		IL_0006: nop
		IL_0007: ldarg.0
		IL_0008: ldarg.1
		IL_0009: stfld int32 System.Runtime.CompilerServices.RefSafetyRulesAttribute::Version
		IL_000e: ret
	} // end of method RefSafetyRulesAttribute::.ctor

} // end of class System.Runtime.CompilerServices.RefSafetyRulesAttribute

.class private auto ansi beforefieldinit Program
	extends [System.Runtime]System.Object
{
	// Nested Types
	.class nested private auto ansi abstract sealed beforefieldinit '<>o__0'
		extends [System.Runtime]System.Object
	{
		.custom instance void [System.Runtime]System.Runtime.CompilerServices.CompilerGeneratedAttribute::.ctor() = (
			01 00 00 00
		)
		// Fields
		.field public static class [System.Linq.Expressions]System.Runtime.CompilerServices.CallSite`1<class [System.Runtime]System.Action`3<class [System.Linq.Expressions]System.Runtime.CompilerServices.CallSite, class [System.Collections]System.Collections.Generic.HashSet`1<string>, object>> '<>p__0'
		.custom instance void System.Runtime.CompilerServices.NullableAttribute::.ctor(uint8[]) = (
			01 00 06 00 00 00 00 00 00 00 01 00 00 00
		)
		.field public static class [System.Linq.Expressions]System.Runtime.CompilerServices.CallSite`1<class [System.Runtime]System.Action`3<class [System.Linq.Expressions]System.Runtime.CompilerServices.CallSite, class [System.Collections]System.Collections.Generic.HashSet`1<string>, object>> '<>p__1'
		.custom instance void System.Runtime.CompilerServices.NullableAttribute::.ctor(uint8[]) = (
			01 00 06 00 00 00 00 00 00 00 01 00 00 00
		)

	} // end of class <>o__0

	.class nested private auto ansi abstract sealed beforefieldinit '<>o__1'
		extends [System.Runtime]System.Object
	{
		.custom instance void [System.Runtime]System.Runtime.CompilerServices.CompilerGeneratedAttribute::.ctor() = (
			01 00 00 00
		)
		// Fields
		.field public static class [System.Linq.Expressions]System.Runtime.CompilerServices.CallSite`1<class [System.Runtime]System.Func`3<class [System.Linq.Expressions]System.Runtime.CompilerServices.CallSite, object, class [System.Collections]System.Collections.Generic.HashSet`1<string>>> '<>p__0'
		.custom instance void System.Runtime.CompilerServices.NullableAttribute::.ctor(uint8[]) = (
			01 00 06 00 00 00 00 00 00 00 00 01 00 00
		)

	} // end of class <>o__1


	// Methods
	.method private hidebysig static 
		object Process (
			object el1,
			object el2
		) cil managed 
	{
		.custom instance void System.Runtime.CompilerServices.NullableContextAttribute::.ctor(uint8) = (
			01 00 01 00 00
		)
		.param [0]
			.custom instance void [System.Linq.Expressions]System.Runtime.CompilerServices.DynamicAttribute::.ctor() = (
				01 00 00 00
			)
		.param [1]
			.custom instance void [System.Linq.Expressions]System.Runtime.CompilerServices.DynamicAttribute::.ctor() = (
				01 00 00 00
			)
		.param [2]
			.custom instance void [System.Linq.Expressions]System.Runtime.CompilerServices.DynamicAttribute::.ctor() = (
				01 00 00 00
			)
		// Method begins at RVA 0x20a4
		// Header size: 12
		// Code size: 201 (0xc9)
		.maxstack 9
		.locals init (
			[0] class [System.Collections]System.Collections.Generic.HashSet`1<string>,
			[1] object
		)

		IL_0000: nop
		IL_0001: newobj instance void class [System.Collections]System.Collections.Generic.HashSet`1<string>::.ctor()
		IL_0006: stloc.0
		IL_0007: ldsfld class [System.Linq.Expressions]System.Runtime.CompilerServices.CallSite`1<class [System.Runtime]System.Action`3<class [System.Linq.Expressions]System.Runtime.CompilerServices.CallSite, class [System.Collections]System.Collections.Generic.HashSet`1<string>, object>> Program/'<>o__0'::'<>p__0'
		IL_000c: brfalse.s IL_0010

		IL_000e: br.s IL_004e

		IL_0010: ldc.i4 256
		IL_0015: ldstr "Add"
		IL_001a: ldnull
		IL_001b: ldtoken Program
		IL_0020: call class [System.Runtime]System.Type [System.Runtime]System.Type::GetTypeFromHandle(valuetype [System.Runtime]System.RuntimeTypeHandle)
		IL_0025: ldc.i4.2
		IL_0026: newarr [Microsoft.CSharp]Microsoft.CSharp.RuntimeBinder.CSharpArgumentInfo
		IL_002b: dup
		IL_002c: ldc.i4.0
		IL_002d: ldc.i4.1
		IL_002e: ldnull
		IL_002f: call class [Microsoft.CSharp]Microsoft.CSharp.RuntimeBinder.CSharpArgumentInfo [Microsoft.CSharp]Microsoft.CSharp.RuntimeBinder.CSharpArgumentInfo::Create(valuetype [Microsoft.CSharp]Microsoft.CSharp.RuntimeBinder.CSharpArgumentInfoFlags, string)
		IL_0034: stelem.ref
		IL_0035: dup
		IL_0036: ldc.i4.1
		IL_0037: ldc.i4.0
		IL_0038: ldnull
		IL_0039: call class [Microsoft.CSharp]Microsoft.CSharp.RuntimeBinder.CSharpArgumentInfo [Microsoft.CSharp]Microsoft.CSharp.RuntimeBinder.CSharpArgumentInfo::Create(valuetype [Microsoft.CSharp]Microsoft.CSharp.RuntimeBinder.CSharpArgumentInfoFlags, string)
		IL_003e: stelem.ref
		IL_003f: call class [System.Linq.Expressions]System.Runtime.CompilerServices.CallSiteBinder [Microsoft.CSharp]Microsoft.CSharp.RuntimeBinder.Binder::InvokeMember(valuetype [Microsoft.CSharp]Microsoft.CSharp.RuntimeBinder.CSharpBinderFlags, string, class [System.Runtime]System.Collections.Generic.IEnumerable`1<class [System.Runtime]System.Type>, class [System.Runtime]System.Type, class [System.Runtime]System.Collections.Generic.IEnumerable`1<class [Microsoft.CSharp]Microsoft.CSharp.RuntimeBinder.CSharpArgumentInfo>)
		IL_0044: call class [System.Linq.Expressions]System.Runtime.CompilerServices.CallSite`1<!0> class [System.Linq.Expressions]System.Runtime.CompilerServices.CallSite`1<class [System.Runtime]System.Action`3<class [System.Linq.Expressions]System.Runtime.CompilerServices.CallSite, class [System.Collections]System.Collections.Generic.HashSet`1<string>, object>>::Create(class [System.Linq.Expressions]System.Runtime.CompilerServices.CallSiteBinder)
		IL_0049: stsfld class [System.Linq.Expressions]System.Runtime.CompilerServices.CallSite`1<class [System.Runtime]System.Action`3<class [System.Linq.Expressions]System.Runtime.CompilerServices.CallSite, class [System.Collections]System.Collections.Generic.HashSet`1<string>, object>> Program/'<>o__0'::'<>p__0'

		IL_004e: ldsfld class [System.Linq.Expressions]System.Runtime.CompilerServices.CallSite`1<class [System.Runtime]System.Action`3<class [System.Linq.Expressions]System.Runtime.CompilerServices.CallSite, class [System.Collections]System.Collections.Generic.HashSet`1<string>, object>> Program/'<>o__0'::'<>p__0'
		IL_0053: ldfld !0 class [System.Linq.Expressions]System.Runtime.CompilerServices.CallSite`1<class [System.Runtime]System.Action`3<class [System.Linq.Expressions]System.Runtime.CompilerServices.CallSite, class [System.Collections]System.Collections.Generic.HashSet`1<string>, object>>::Target
		IL_0058: ldsfld class [System.Linq.Expressions]System.Runtime.CompilerServices.CallSite`1<class [System.Runtime]System.Action`3<class [System.Linq.Expressions]System.Runtime.CompilerServices.CallSite, class [System.Collections]System.Collections.Generic.HashSet`1<string>, object>> Program/'<>o__0'::'<>p__0'
		IL_005d: ldloc.0
		IL_005e: ldarg.0
		IL_005f: callvirt instance void class [System.Runtime]System.Action`3<class [System.Linq.Expressions]System.Runtime.CompilerServices.CallSite, class [System.Collections]System.Collections.Generic.HashSet`1<string>, object>::Invoke(!0, !1, !2)
		IL_0064: nop
		IL_0065: ldsfld class [System.Linq.Expressions]System.Runtime.CompilerServices.CallSite`1<class [System.Runtime]System.Action`3<class [System.Linq.Expressions]System.Runtime.CompilerServices.CallSite, class [System.Collections]System.Collections.Generic.HashSet`1<string>, object>> Program/'<>o__0'::'<>p__1'
		IL_006a: brfalse.s IL_006e

		IL_006c: br.s IL_00ac

		IL_006e: ldc.i4 256
		IL_0073: ldstr "Add"
		IL_0078: ldnull
		IL_0079: ldtoken Program
		IL_007e: call class [System.Runtime]System.Type [System.Runtime]System.Type::GetTypeFromHandle(valuetype [System.Runtime]System.RuntimeTypeHandle)
		IL_0083: ldc.i4.2
		IL_0084: newarr [Microsoft.CSharp]Microsoft.CSharp.RuntimeBinder.CSharpArgumentInfo
		IL_0089: dup
		IL_008a: ldc.i4.0
		IL_008b: ldc.i4.1
		IL_008c: ldnull
		IL_008d: call class [Microsoft.CSharp]Microsoft.CSharp.RuntimeBinder.CSharpArgumentInfo [Microsoft.CSharp]Microsoft.CSharp.RuntimeBinder.CSharpArgumentInfo::Create(valuetype [Microsoft.CSharp]Microsoft.CSharp.RuntimeBinder.CSharpArgumentInfoFlags, string)
		IL_0092: stelem.ref
		IL_0093: dup
		IL_0094: ldc.i4.1
		IL_0095: ldc.i4.0
		IL_0096: ldnull
		IL_0097: call class [Microsoft.CSharp]Microsoft.CSharp.RuntimeBinder.CSharpArgumentInfo [Microsoft.CSharp]Microsoft.CSharp.RuntimeBinder.CSharpArgumentInfo::Create(valuetype [Microsoft.CSharp]Microsoft.CSharp.RuntimeBinder.CSharpArgumentInfoFlags, string)
		IL_009c: stelem.ref
		IL_009d: call class [System.Linq.Expressions]System.Runtime.CompilerServices.CallSiteBinder [Microsoft.CSharp]Microsoft.CSharp.RuntimeBinder.Binder::InvokeMember(valuetype [Microsoft.CSharp]Microsoft.CSharp.RuntimeBinder.CSharpBinderFlags, string, class [System.Runtime]System.Collections.Generic.IEnumerable`1<class [System.Runtime]System.Type>, class [System.Runtime]System.Type, class [System.Runtime]System.Collections.Generic.IEnumerable`1<class [Microsoft.CSharp]Microsoft.CSharp.RuntimeBinder.CSharpArgumentInfo>)
		IL_00a2: call class [System.Linq.Expressions]System.Runtime.CompilerServices.CallSite`1<!0> class [System.Linq.Expressions]System.Runtime.CompilerServices.CallSite`1<class [System.Runtime]System.Action`3<class [System.Linq.Expressions]System.Runtime.CompilerServices.CallSite, class [System.Collections]System.Collections.Generic.HashSet`1<string>, object>>::Create(class [System.Linq.Expressions]System.Runtime.CompilerServices.CallSiteBinder)
		IL_00a7: stsfld class [System.Linq.Expressions]System.Runtime.CompilerServices.CallSite`1<class [System.Runtime]System.Action`3<class [System.Linq.Expressions]System.Runtime.CompilerServices.CallSite, class [System.Collections]System.Collections.Generic.HashSet`1<string>, object>> Program/'<>o__0'::'<>p__1'

		IL_00ac: ldsfld class [System.Linq.Expressions]System.Runtime.CompilerServices.CallSite`1<class [System.Runtime]System.Action`3<class [System.Linq.Expressions]System.Runtime.CompilerServices.CallSite, class [System.Collections]System.Collections.Generic.HashSet`1<string>, object>> Program/'<>o__0'::'<>p__1'
		IL_00b1: ldfld !0 class [System.Linq.Expressions]System.Runtime.CompilerServices.CallSite`1<class [System.Runtime]System.Action`3<class [System.Linq.Expressions]System.Runtime.CompilerServices.CallSite, class [System.Collections]System.Collections.Generic.HashSet`1<string>, object>>::Target
		IL_00b6: ldsfld class [System.Linq.Expressions]System.Runtime.CompilerServices.CallSite`1<class [System.Runtime]System.Action`3<class [System.Linq.Expressions]System.Runtime.CompilerServices.CallSite, class [System.Collections]System.Collections.Generic.HashSet`1<string>, object>> Program/'<>o__0'::'<>p__1'
		IL_00bb: ldloc.0
		IL_00bc: ldarg.1
		IL_00bd: callvirt instance void class [System.Runtime]System.Action`3<class [System.Linq.Expressions]System.Runtime.CompilerServices.CallSite, class [System.Collections]System.Collections.Generic.HashSet`1<string>, object>::Invoke(!0, !1, !2)
		IL_00c2: nop
		IL_00c3: ldloc.0
		IL_00c4: stloc.1
		IL_00c5: br.s IL_00c7

		IL_00c7: ldloc.1
		IL_00c8: ret
	} // end of method Program::Process

	.method private hidebysig static 
		void Main () cil managed 
	{
		// Method begins at RVA 0x217c
		// Header size: 12
		// Code size: 142 (0x8e)
		.maxstack 4
		.entrypoint
		.locals init (
			[0] string,
			[1] string,
			[2] class [System.Collections]System.Collections.Generic.HashSet`1<string>,
			[3] valuetype [System.Collections]System.Collections.Generic.HashSet`1/Enumerator<string>,
			[4] string
		)

		IL_0000: nop
		IL_0001: ldstr "banana"
		IL_0006: stloc.0
		IL_0007: ldstr "apple"
		IL_000c: stloc.1
		IL_000d: ldsfld class [System.Linq.Expressions]System.Runtime.CompilerServices.CallSite`1<class [System.Runtime]System.Func`3<class [System.Linq.Expressions]System.Runtime.CompilerServices.CallSite, object, class [System.Collections]System.Collections.Generic.HashSet`1<string>>> Program/'<>o__1'::'<>p__0'
		IL_0012: brfalse.s IL_0016

		IL_0014: br.s IL_003a

		IL_0016: ldc.i4.0
		IL_0017: ldtoken class [System.Collections]System.Collections.Generic.HashSet`1<string>
		IL_001c: call class [System.Runtime]System.Type [System.Runtime]System.Type::GetTypeFromHandle(valuetype [System.Runtime]System.RuntimeTypeHandle)
		IL_0021: ldtoken Program
		IL_0026: call class [System.Runtime]System.Type [System.Runtime]System.Type::GetTypeFromHandle(valuetype [System.Runtime]System.RuntimeTypeHandle)
		IL_002b: call class [System.Linq.Expressions]System.Runtime.CompilerServices.CallSiteBinder [Microsoft.CSharp]Microsoft.CSharp.RuntimeBinder.Binder::Convert(valuetype [Microsoft.CSharp]Microsoft.CSharp.RuntimeBinder.CSharpBinderFlags, class [System.Runtime]System.Type, class [System.Runtime]System.Type)
		IL_0030: call class [System.Linq.Expressions]System.Runtime.CompilerServices.CallSite`1<!0> class [System.Linq.Expressions]System.Runtime.CompilerServices.CallSite`1<class [System.Runtime]System.Func`3<class [System.Linq.Expressions]System.Runtime.CompilerServices.CallSite, object, class [System.Collections]System.Collections.Generic.HashSet`1<string>>>::Create(class [System.Linq.Expressions]System.Runtime.CompilerServices.CallSiteBinder)
		IL_0035: stsfld class [System.Linq.Expressions]System.Runtime.CompilerServices.CallSite`1<class [System.Runtime]System.Func`3<class [System.Linq.Expressions]System.Runtime.CompilerServices.CallSite, object, class [System.Collections]System.Collections.Generic.HashSet`1<string>>> Program/'<>o__1'::'<>p__0'

		IL_003a: ldsfld class [System.Linq.Expressions]System.Runtime.CompilerServices.CallSite`1<class [System.Runtime]System.Func`3<class [System.Linq.Expressions]System.Runtime.CompilerServices.CallSite, object, class [System.Collections]System.Collections.Generic.HashSet`1<string>>> Program/'<>o__1'::'<>p__0'
		IL_003f: ldfld !0 class [System.Linq.Expressions]System.Runtime.CompilerServices.CallSite`1<class [System.Runtime]System.Func`3<class [System.Linq.Expressions]System.Runtime.CompilerServices.CallSite, object, class [System.Collections]System.Collections.Generic.HashSet`1<string>>>::Target
		IL_0044: ldsfld class [System.Linq.Expressions]System.Runtime.CompilerServices.CallSite`1<class [System.Runtime]System.Func`3<class [System.Linq.Expressions]System.Runtime.CompilerServices.CallSite, object, class [System.Collections]System.Collections.Generic.HashSet`1<string>>> Program/'<>o__1'::'<>p__0'
		IL_0049: ldloc.0
		IL_004a: ldloc.1
		IL_004b: call object Program::Process(object, object)
		IL_0050: callvirt instance !2 class [System.Runtime]System.Func`3<class [System.Linq.Expressions]System.Runtime.CompilerServices.CallSite, object, class [System.Collections]System.Collections.Generic.HashSet`1<string>>::Invoke(!0, !1)
		IL_0055: stloc.2
		IL_0056: nop
		IL_0057: ldloc.2
		IL_0058: callvirt instance valuetype [System.Collections]System.Collections.Generic.HashSet`1/Enumerator<!0> class [System.Collections]System.Collections.Generic.HashSet`1<string>::GetEnumerator()
		IL_005d: stloc.3
		.try
		{
			IL_005e: br.s IL_0073
			// loop start (head: IL_0073)
				IL_0060: ldloca.s 3
				IL_0062: call instance !0 valuetype [System.Collections]System.Collections.Generic.HashSet`1/Enumerator<string>::get_Current()
				IL_0067: stloc.s 4
				IL_0069: nop
				IL_006a: ldloc.s 4
				IL_006c: call void [System.Console]System.Console::WriteLine(string)
				IL_0071: nop
				IL_0072: nop

				IL_0073: ldloca.s 3
				IL_0075: call instance bool valuetype [System.Collections]System.Collections.Generic.HashSet`1/Enumerator<string>::MoveNext()
				IL_007a: brtrue.s IL_0060
			// end loop

			IL_007c: leave.s IL_008d
		} // end .try
		finally
		{
			IL_007e: ldloca.s 3
			IL_0080: constrained. valuetype [System.Collections]System.Collections.Generic.HashSet`1/Enumerator<string>
			IL_0086: callvirt instance void [System.Runtime]System.IDisposable::Dispose()
			IL_008b: nop
			IL_008c: endfinally
		} // end handler

		IL_008d: ret
	} // end of method Program::Main

	.method public hidebysig specialname rtspecialname 
		instance void .ctor () cil managed 
	{
		// Method begins at RVA 0x2228
		// Header size: 1
		// Code size: 8 (0x8)
		.maxstack 8

		IL_0000: ldarg.0
		IL_0001: call instance void [System.Runtime]System.Object::.ctor()
		IL_0006: nop
		IL_0007: ret
	} // end of method Program::.ctor

} // end of class Program

