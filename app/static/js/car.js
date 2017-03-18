
$(document).ready(function () {

	//jquery特效制作复选框全选反选取消(无插件)
	// 全选        
	$(".gou").click(function () {   
		if ($(this).attr("checked")) {
			$(".TheShoppingCartData input[name=newslist]").each(function () {
			$(this).attr("checked", true);
			GetCount();
			});
		}else{
			$(".TheShoppingCartData input[name=newslist]").each(function () {
			$(this).attr("checked", false);
		});
		}
		
		
	});


});
//******************
function GetCount() {
	var conts = 0;
	var aa = 0;
	$(".gou input[name=newslist]").each(function () {
		if ($(this).attr("checked")) {
			for (var i = 0; i < $(this).length; i++) {
				conts += parseInt($(this).val());
				aa += 1;
			}
		}
	});
	$("#shuliang").text(aa);
	$("#zong1").html((conts).toFixed(2));
	$("#jz1").css("display", "none");
	$("#jz2").css("display", "block");
}



	$(function () {
		var t = $("#");
		$("").click(function () {
		// $("#add1").click(function () {
			$this.val(parseInt(t.val()) + 1)
			setTotal(); GetCount();
		})
		$("#min1").click(function () {
			t.val(parseInt(t.val()) - 1)
			setTotal(); GetCount();
		})
		function setTotal() {

			$("#total1").html((parseInt(t.val()) * 9).toFixed(2));
			$("#newslist-1").val(parseInt(t.val()) * 9);
		}
		setTotal();
	})



	$(function () {
		$(".quanxun").click(function () {
			setTotal();
			//alert($(lens[0]).text());
		});
		function setTotal() {
			var len = $(".tot");
			var num = 0;
			for (var i = 0; i < len.length; i++) {
				num = parseInt(num) + parseInt($(len[i]).text());

			}
			//alert(len.length);
			$("#zong1").text(parseInt(num).toFixed(2));
			$("#shuliang").text(len.length);
		}
		//setTotal();
	})


