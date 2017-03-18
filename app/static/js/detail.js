//商品详情
$(function(){
	var oCollect=0	
	$(".collectionBtn").click(function(){
		if(oCollect==0)
		{
			++oCollect
			$(this).addClass("collectionBtnClick")
		}
		else
		{
			oCollect=0
			$(this).removeClass("collectionBtnClick")
		}
	})
})

//商品详情 购物车
$(function(){
	var oGsc=0
	$(".XZCC").click(function(){
		$(".GWC").slideDown(333)
	})
	$(".goShoppingcartBtn").click(function(){
		$(".GWC").slideDown(333)
	})
	$(".EscBtn").click(function(){
		$(".layerBox").slideUp(333)
	})
	$(".specifications p").click(function(){
		++oGsc
		$(".specifications p").css({"background":"#eaeaea","color":"#333"})
		$(this).css({"background":"#f9b40e","color":"#fff"})
	})
	$(".buyBtn").click(function(){
		if(oGsc!=0)
		{
			$(".layerBox").hide(333)
		}
		else
		{
			alert("你还没有选择规格")
		}
	})
})

//商品详情 优惠券
$(function(){
	$(".couponsIndex").click(function(){
		$(".YHQ").slideDown(333)
	})
})

//订单提交
$(function(){
	$(".settlement").click(function(){
		$(".XZSHDZ").slideDown(333)
	})
	$(".SelectAddressBtn").click(function(){
		$(".XZSHDZ").fadeOut(333)
		$(".FKXQ").slideDown(333)
	})
})

//订单详情 收货地址
$(function(){
	$(".addressIndex").click(function(){
		$(".SHDZ").slideDown(333)
	})
	$(".defaultAddress").click(function(){
		$(".SHDZ").hide(333)
	})
	
	
	$(".addressIndex1").click(function(){
		$(".SHDZ1").slideDown(333)
		$(".XZSHDZ").hide()
	})
	$(".defaultAddress").click(function(){
		$(".SHDZ1").hide(333)
		
	})
	
	
	var oDe=0
	$(".defaultBtnBox").click(function(){
		if(oDe==0)
		{
			++oDe
			$(".defaultBtnBox").addClass("defaultBtnClick")
			$(".defaultBtn").animate({left:20},222)
		}
		else
		{
			oDe=0
			$(".defaultBtnBox").removeClass("defaultBtnClick")
			$(".defaultBtn").animate({left:1},222)
		}
	})
	
	$(".SelectAddressTxt").click(function(){
		$(".SelectAddressTxt").removeClass("SelectAddressTxtClick")
		$(this).addClass("SelectAddressTxtClick")
	})
})
