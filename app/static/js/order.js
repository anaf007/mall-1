// JavaScript Document

//订单Tab
$(function(){
	$(".orderTab p:first").css("color","#ff0000")
	$(".orderTab p").click(function(){
		oRder=$(".orderTab p").index(this)
		$(".orderTab p").css("color","#333")
		$(this).css("color","#ff0000")
		if(oRder==0)
		{
			$(".orderIndex").show(333)
		}
		else
		{
			--oRder
			$(".orderIndex").slideUp(0)
			$(".orderIndex").eq(oRder).show(333)
		}
	})
})

//购物车
$(function(){
	$(".TheEditorIndex").click(function(){
		oTheEditor=$(".TheEditorIndex").index(this)
		if($(".TheEditor").eq(oTheEditor).is(":visible")==false)
		{
			$(".TheEditor").eq(oTheEditor).show(555)
		}
		else
		{
			$(".TheEditor").eq(oTheEditor).hide(333)
		}
	})
})

//积分兑换
$(function(){
	$(".PointsForNumber").each(function(){
		if($(this).text()>0)
		{
			$(this).css("color","#0d7600")
		}
		else
		{
			$(this).css("color","#f90000")
		}
	})
})

//优惠券Tab
$(function(){
	$(".couponsTab a:first").css({"color":"#f1565e","border-bottom":"1px solid #f1565e"})
	$(".couponsBox:first").show()
	$(".couponsTab a").click(function(){
		oCpu=$(".couponsTab a").index(this)
		$(".couponsTab a").css({"color":"#333","border-bottom":"1px solid transparent"})
		$(this).css({"color":"#f1565e","border-bottom":"1px solid #f1565e"})
		if($(".couponsBox").eq(oCpu).is(":visible")==false)
		{
			$(".couponsBox").slideUp(333)
			$(".couponsBox").eq(oCpu).slideDown(333)
		}
	})
})


















