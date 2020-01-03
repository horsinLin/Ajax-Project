/**
 * Created by horsin on 20-1-1
 */
function createXhr() {
    if(window.XMLHttpRequest){
        return new XMLHttpRequest()
    }else{
        return new ActiveXObject("Microsoft.XMLHTTP")
    }
}


