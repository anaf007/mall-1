/*商品分类*/
$(function () {
    var oHeight = $(window).height()
    oHeight = oHeight - 41
    $(".goodsListBox").height(oHeight)
    $(".goodsListLeft").height(oHeight)
    $(".goodsListRight").height(oHeight)
})
//商品列表
$(function () {
    var oGl = 0;
    $(".GLindex").eq(oGl).addClass("GLindexClick")
    $(".goodsListRight").eq(oGl).show()
    $(".GLindex").click(function () {
        oGl = $(".GLindex").index(this)
        $(".GLindex").removeClass("GLindexClick").eq(oGl).addClass("GLindexClick")
        //$(".GLindex").eq(oGl).addClass("GLindexClick")
        $(".goodsListRight").hide().eq(oGl).show()
        //$(".goodsListRight").eq(oGl).show()	
    })
})
/*商品分类 end*/


/*切换浏览模式:列表*/
function changeCl(cls) {
    var vl = cls.getAttribute('class');
    var lst = document.getElementById('List_box');
    switch (vl) {
        case "switchBtn switchBtn_list":
            cls.setAttribute('class', 'switchBtn switchBtn_grid');
            lst.setAttribute('class', 'grid');
            document.getElementById('display').setAttribute('value', 'grid');
            break;
        case "switchBtn switchBtn_grid":
            cls.setAttribute('class', 'switchBtn switchBtn_list');
            lst.setAttribute('class', 'list');
            document.getElementById('display').setAttribute('value', 'list');
            break;

    }
}
/*切换浏览模式:列表 end*/

//商品列表 -1
$(function () {
    var oPr = 0;
    $(".goodsList-2 p").click(function () {
        $(".priceBtn").removeClass("priceBtnClickDown")
        $(".priceBtn").removeClass("priceBtnClick")
        $(".goodsList-2 p").css("color", "#666")
        $(this).css("color", "#ff4c4f")
    })
    $(".priceBtn").click(function () {
        if (oPr == 0) {
            $(".goodsList-2 p").css("color", "#666")
            ++oPr
            $(".priceBtn").removeClass("priceBtnClickDown")
            $(".priceBtn").removeClass("priceBtnClick")
            $(".priceBtn").addClass("priceBtnClick")
        }
        else {
            $(".goodsList-2 p").css("color", "#666")
            oPr = 0
            $(".priceBtn").removeClass("priceBtnClick")
            $(".priceBtn").addClass("priceBtnClickDown")
        }
    })
})