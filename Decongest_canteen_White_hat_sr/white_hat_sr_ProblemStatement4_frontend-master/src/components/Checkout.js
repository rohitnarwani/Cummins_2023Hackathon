import React, {useState} from "react"
import styles from "./Checkout.module.css"
import FoodCard from "./FoodCard.js"
import  DtPicker  from 'react-calendar-datetime-picker'
import PortionButton from "./PortionButton.js"
import 'react-calendar-datetime-picker/dist/index.css'

const DatePicker = ({reqHandler, _handler, _count}) => {
  const [date, setDate] = useState(null)
  reqHandler(date, _count)
  return (
      <div className={styles.righti}>
    <DtPicker
      onChange={setDate}
      placeHolder="Select Time"
      withTime
      showTimeInput
    />
      <span>Number of Seats:</span>
      <div className={styles.hello}>
        <PortionButton handler={_handler} currentCount={_count}/>
      </div>
    </div>
  )
}

function Checkout({getVal, inCart, cardHandler, doneFunc, reqHandler}) {
    // let [ goToHome, setHome ] = useState(false);
    let [ _count, setCount ] = useState(1);

    function _handler(name, count) {
        if (count >= 4) {
            setCount(1);
        }
        setCount(count);
    }
    const menu = [

      { id: 1,  name: "Pohe",         price: 25, img:"https://as2.ftcdn.net/v2/jpg/04/72/01/73/1000_F_472017398_v6JPATak7p8VenbHzoW3O0PhGA3fircQ.jpg"},
      { id: 2,  name: "Idli",         price: 40, img:"https://as2.ftcdn.net/v2/jpg/04/26/94/99/1000_F_426949957_iFC4zrETHm1lFMiLpsVXeAhFQe6vCNAk.jpg"},
      { id: 3,  name: "Dosa",         price: 50, img:"data:image/jpeg;base64,/9j/4AAQSkZJRgABAQAAAQABAAD/2wCEAAkGBwgHBgkIBwgKCgkLDRYPDQwMDRsUFRAWIB0iIiAdHx8kKDQsJCYxJx8fLT0tMTU3Ojo6Iys/RD84QzQ5OjcBCgoKDQwNGg8PGjclHyU3Nzc3Nzc3Nzc3Nzc3Nzc3Nzc3Nzc3Nzc3Nzc3Nzc3Nzc3Nzc3Nzc3Nzc3Nzc3Nzc3N//AABEIAH8AvQMBIgACEQEDEQH/xAAbAAABBQEBAAAAAAAAAAAAAAAEAAMFBgcBAv/EAEoQAAECBQIDBAYHAgoKAwAAAAECAwAEBREhEjEGQVETImFxFDJCgZGhBxVSscHR0iOiM0NiY3OChJLh8BY0RFNVZHJ0wvEXJCX/xAAaAQACAwEBAAAAAAAAAAAAAAACBAEDBQAG/8QAJhEAAgEEAgEEAgMAAAAAAAAAAQIAAwQRIRIxQRMUIlEFMmFxgf/aAAwDAQACEQMRAD8A3GFChR06KFChR06KFChR06KFChR06KFChR06KFChR06KFHIFqNRlabLqmJ19DTY5k5PgBziCQBucBmFXgaan5OTGqbmmWR/OLCYz2t8czk+os0lKpVj/AHqh+0V5DZI+flENLtJmFF111bj3tLWoqPxMIVr9U0u45Ts3YZbU1Vms018gMzzCidu+IOSoKF0kEdRGXMskEAW0kbiJOmT81JKHYqsi+Uk90+6F6f5QZw6w3siB8TNAhQJT5xM7Lh1GDspPQwVeNZWDDIiJBBwZ2FHCbQDNVinSd/SZ6XbI3BcF/hEkgdyIfCisTXHVDYJSh9x9Q5NNk/M2EREz9JTCFgS1OdWnmXFhP3Xis1kHmCWAl9uI7e8Y1J8f12bU88X20WX3WktDSB0zn5xfOGeLWamBLzmhmb5Zslzy8fCIFdS3GCKqk4lphR5vEVXeIqZQmC7UJgJV7LScrX5D/Ii0kDuWSWuIV4yqq8fVKfWUSKRIy5ODhTqh57D3RENVapLBUqoTZVcbvK/OF3uVXqUPXVZtl4V4xVVbqiQNNRmgf6Uww7XqjqSTUZsnweVA+6H1IFwD4m43jsYWK9Vv+JTY8nlfnCPEdWSBeqzl/wCmMT7ofUMVQZul4amJhmWZU7MOobbTkrWbARhKuI664sJZqE6SejqodSxVp+yp+Yfdsb2fcUq3kDFb3yqI/QtHqbOhL5WePmkqUxRWi+vbt1A6R5DnFVcMzUH/AEmouredOxWDgdANhCYprg7qnuWwxaHW2S0khDygUjKTcGMivdtU7M1aVvTp/rOAMoshIt4HYQY0w2spQU3K8JUMGBxrWrS4kKT5ZESUloCQV99sq5coTY7lrDiI1LtKS6dIVdAwCfjEqlq6CbC98qttHeyVrQqwsk4AwT5QVpQG9BSdJGYOku9xZ3gq6q/QZN+YYYS9a10KUUi17X2iAnePqy9dDKmWOpbbuR/evEjxIsJpU2AbXZ0i/W+IoW11HzjVt6rcMZ1MP8gxWoMeYXN1iozwtNT0w6DyW4bH3bRHglCTgbx7tYgDPQx0pxptcGLDuICofMaDlyTvHhbhJj2prvd04hspUk5EEAIYYGOyjKWUrAJ1arkRKIVY+YERKFlMwq/MCJNohWnPKAeUvkHMMNaqrVmkVKbS3Y90PHpFfmS5MTDqlOKcUpRutRuT74kpiwTe+RADS0tqI98SrGGjEiEFN1JUrGAY99r2YPU7QM66paeghpKrkXO4iAMzuGe46t5ar8hDZXjyhWK7hAuefQecFyNOVMLBXdQv7v8AGBZ1QZMdt7SpV/UagjfaOn9mLjryg2WpK3CkvFWRfSn/ADiJmVkUJyq6bHyMFlBbICEqI6g7wlVu86E3Leyp0tnZgctLtM4SgAg7J3iQaXdWlIWCPZ6x4SgglWnSB1EEoWsZSCDzUBCLuTHSIUqXuQUj1hnMDpp6gsErTqvfSs2xDyHX7BKLDkT184Ll5IrSCuywd74OfGITJ6lWSo2ZGpllv6sC6bC6YLYly1KkHcnYjN7xJmWbRL6VaQkDYK3gfKlpVukHup5kxLKR3ANUsMR5R0GylDVbZWRiH0JW8AhkKJt8POPMlK+kukrcQhHNSsX8ol1vSsg32aClZI9VJz8Y1LOzZ/k+hEK9bjodyr8ScPz0/LBMtMpCxlUuoABy2R3uXkceUUV2mzzC1svSMyCj1h2RsPftGmTVVdbnUSzbCFLUnWSUlSU/ycc9or9QnZlyWWJ0uqfWsJSkA2SScY2HlFte4o0/jTG4k1sax5MZVG6bOqQbScwQnBIbJ+6GSm2FXSoHKSLGJyYnpxqmOuSrzyXgvQQi4KU35Wj1RdSJJz60Sh4OuFZDqdSiNgb7g88GK1uBxyZS9kQcKZAFscueYZcCknYmJyfpKTKqmqdqPZjU5LXupsWzY+1bN84iGLwSBcA36mL0bkMiJOjIcGDPp0vJPUFMPyr1kXJGD/jAzzuvNsA3htCiNSeW8W8ciFwyMGHPudpqAODAtu+Ffax8Y9agEg33xBctTJiYA1JLaN8+t8OUByVBuXUqLOeKiCXJOkDUo7AQVKUxxwJU+bJ6Jz90TUnTG2QSElOMknfzvBIkW0OFTSU6ugNoTqXXhZr29gi7fZgH1aEtlKbEdIJlWi0kDQRjfnB2lV7A5tax5w7odwLWA6ZhFqjNNVcKMCDIcVbvpuQOcPsOMi6tOgeEJu6VW7o53t8ecEBSVgDs045xS0JsfU9IebdwCNP3w+12a06SVFR2ziONywBJSlJtvbMEhttoG4ItjaBVR2ZSzjoT0yyw25k3sfazBTj6OyWUJKtO3MHwhg6AlSgnJG3SHZKVmJmyG045k8obpqSeFMSh2HZMGDrjiCXgEjki9rDqY9BtTqr5SjkdifyiZmqYzLSwcKNak5K1HF/KIta1PlQQQhlA1OOLwlA6kxpULAIc1NmKPccv16jbjwR+yYSCeoimcV8ZNUtZkpVSXpkH9qfZQOdz13xAHFnGSilyQ4eWQ0bpcn7WK87IB2Hj8OsZ4UEXK/eSd41VTyYmX+ptU3U/R6k7Ltp0h49sytQuCFfZPhke6GpZqdcmHX3HmnEk91FySPHoDEHwpUmK3SG5CfeKJqWw26kjVp5KHyBHO0WumyMwwl1Lig+VLJS82Qmw5EpJ69Lxg3lq9Lk9MZzG1dHXc65MJUye7pXbCiM+6GpmnuOIafRpAISTptcW64584In5Z5xapYtuJAzexHzhwy77kgGpdLpetnSkkgjx+MZ6IwPxE5mGNR15DTTSplpISW+8lCdwRy/CKlVeHVNVSbQw80hgOns02vpBzb3XtFs9HNMpzk9WtIQg6ky4IKnl7pT8QIzyZmpmZeW868VLWoqVrJFiTc2jVtaNSih5+Zm3VRNCRe4tBMnITM2dbTelvYuLwD5dYAU4MeUWuiMTwkUCbQEJSLNJPr25X/LeH6gYLlZNFA7fKckqSGLKTdSuazuPLpEwyylvKB77R4bOkWWDBbaO6CnblGZUBbZmvTZVGAJ1pAPrDPKCOwuO563nHhs2h5KVlI0qtnOL3HSKGp5Et5RpLKlCxSLg732glpo6UpJCCkd4b5jv8WSqwCTyg1thxRSoLVjBTfl0gVoHOpxeCPSzTgspAxnV4fjHRJpCcjXq2gpwoaGQO0B5G4I8oYW/2hQS0lIABuDbEE6InfchWY9To7m4VptvvDRCu0OkFd+8B/n3w6w07NnQwkm5JuOUWKnUtuVAW7ZbvU8oOjZvcH6EGpWFP+4FT6U48A5MjQjkkbkRKPzEtTmQMJ+ykbmB56qBKuxlP2rpxjYRWatWBT5hTLMq7Vqyc+jMpKks+LihgeW8bdKklEYQf7EHqFttJOfmC40ZypPdhKp9VKT3l+CRzihcTVGbraPRg+zI0pJuJZu6ivxcOxPht5w3UKfxnVJhUzPSi9RwErmGUBA6JBXge6Iqa4e4hRdX1c44ercw058gsn5QLMSficRd2dvGpL8K8FydZ7V6Yed9DYVpWsWTqV0H4+cXCap/DvC9KenWKPItNS4TqfmkAk3wO8QScmIj6PXnF0F2kTgekZxmaUoIWgpK0mx2O+5j3xZw5UK1TH5aXmW1JKrBp1xQCgDjyP47RcoKjvMlAPMlajWaG9JIeaYYm0OWDZabTY38SMdI6xLoXItzMqgdg42F3b3AI+zsQPC0Vig8OT0k24/xOw0QAEIEs6SSrm4SNu7gjn0EX1nsG6awtFmmeyAACDpSm2ABy8jmIHLO4TrhsDqVCoVtNNmjLvzaW3LBYCXtIUk7KAvtvDauMw02dJW+q2Bkj3k4tEfxpLoE3JocbKH22VKVzKApRKUn4fOIRtIAv80/jAPcFeojVqFWIENqVRm6u+H5xxV0juI3QgfybbecCaD/AO8/lHoEchjqOUcNzkAnxQbQqzcjkxcsTKtLTvos3LzGgOdk4FaD7Vje0aNT5tioy6ZmTc1oPrD2kHoocjGdppq1essZ6XxBklrpT4mJaaW24NwnZQ6KHMQ47I2gZqI3AzRA2lQ72Yca1M29tN9uYiCpXE8hOlLL6xLzJwNR7i/I8vI/OJ+xSbEWhCqHU7EeRlYakihgOMhxKbp8M3glmVUBcgJ8TziNlZpyVVqbyk+sk84mUTjLrd0C2rrv5GIQKwkMWXUdMuwEalA6hyBgGafJc7hDaR7TZ9bzENzD7mrvH5wy2l2ZXoQkk336RTWPIcU7lqa2YlPG/XVz6iJCnUpyZGt3U20d0ncwbT6ShkhyYOtWwCuUeqjUezPZtnSBjHOGaNjg86sqqXGfikkEGVkWtIKG0jxiHqVWLqVhCuxl0jvrVjHW/KIWs1WVpcoZ2qvdk1nQPaWeiRzMZlW+L5usOqToTLyaf4OXvfV0Kup+QjQ3jQ1FXbG+zNWkqtKpp658ns5JSiGnUmzkxbcp+ynx3PhzqtT45U2DLU1pthgbBsW8yfGBeMJwIlKTLyxCZX0BpTSU8wUxSZmotLV2LndIGFFH4xnOHquQeh4m7ZW9GnTFWpsmWF7iKemCSpxQ8bn84ENWn9YKXnAsHAuREXLPhC0hIW6FC9wNh+ESsmpl+WKvVdCiNKhcgDnjl4wJpqnQjNS6oJo4khJcbzcrpaqLQeY6Kzp8fA+VovEvXTM04zck6mZlDYOtu5W0eVyMkeJyMRnFRaDss3YN9xNgUJtq84d+jmYc+upmmlR9GmJV7tB0AQc/dF9Bz46iN5bU3pGomiJpNPrbSCUNyrTerJIWc/GJSZrtPkGPSZko1gdxAIKlHlb84yOWE+EJJqLjuOekH5CCm21KWFrcW4ra7hzDDXKgaG55hq58R+ozr1RnnpyZFnHlaiB7I2A8bDEDAE5F/NP4w8RpOnHlHMHfB69DCROdmKnZzG7Hc5HVMdsDuptX/VgwlawrI1Hw7p/xjwSo+rp/rozEQwJVnJp1W7ivIQytRVuSYcLaUk5J8hHjA2HxjVAAmhmDq8dol6PxLU6TpaS520tt2LuRbwO4+6I8tKXsk38BDKkEEhQNxyMSQDoyQcdTSqRxZS6jZC3PQ3z/ABb5xfwVt8bRYW1OIP7IHvDbcGMRUg9L+cSVJ4gq9GUFU6dcQkbtrOtHwP4WhV7NCcrqXrXOMHc3WTpLsxpXMDQnex3iZlpVqXRoaSExmFF+lxQSlFakCeRclc/un8IuMpxrQpxsLbn0NLIvpf7hHxi5KKU+u4DVCe5K1Go+iAtt5dI3OwipcQV+V4fa7WcT6TPuDUzIpVYkfaWfZT8zygPiLjGUk0uKpjrU/UV37MjvssfylH2j0T8YzdwuzMw5MzTy3pl1RU664bqUYk97gmoANRquVKdrc8Z+pvdq9bShKRZLSfspHIRFlKlKF9usTDrCSm53iPcQQdrQatmADmXegmW4i4bZpMy6luep4IlnlXsE8gbezy8LRB1KiTcgoM1GVUlBuUuHKFeKVDBiGk33pKabmpdZQ62bpP4HwMaDReKmptnsy4G3SO+wu2lXiAcERRUpZPIR63vTSHFhkSlBlLOpLKy2VZVpAIVt12PlBDbwWRfJTkW3vF0fRTXDqcpUgo9exUi/90iOSgo6XgfqiSCxsdDi/vUYo9EnzGmv7VlwySry7U7UdTNOacmJhR/g2wVG/XwEWmV4fHCdBmVTbqHK1Uk9iEoVcMt3GsDrfYmJhXEUvTZfsmG2kq9lllKUJv46dvfFanJmYnphUzNLK3D7tI6J6CJZVpDvJmbc/keVP0qYwIB2SwO93R1hWUbDvX+yT90FhF7k3Kb4uLfGO9mkjA+ULlpkQdCiB3jcGCEpP9WF2YzY+/rHkKUbIZbKlHpt8IjMJULHU9HSjdWPGOJcWv8AgWysDcgQ8zJEkLfVrIyUA8ucSRYCO6EtpA2GBAnU06FgW/bUiVfR7xEQP/ysj/mG/wBUL/4+4jSoaaQNJ3T27Xx9aN0hRren/MD0hMMHAXE4uBTO6dv27WPD1o6eAOInUWdpd1DY+kNfqjcoUR6Q+53pCYQfo44i04po8Qp9vHv1Q2r6NeJDtTQP7Q3+qN7hQQTHmT6YmCNfRrxC2Cfqy674PpDWP3oLRwFxNcFdO2/n2s/vRt52gCpMTUz2aZaY7JvPaZzysRg9PnziDTB8wTSBmPOfR/xJuzTdPVPbt/qhs8A8U7fVeP8AuGv1Rq/odaW42pyfb7ibdzAUdQNyNPS4t+cexKVktpS5PoKiO9psOXLu9b+6OFICcKSiZIj6PeJr3NN0/wBoaP8A5R136O+I1i/1am/hMN/qjWUylaU42p2dZOhYXYcxzHq8+vLax3j2+xV1vXbnm22+0JIABOjoLp35e6/Ow70gD3J9MTGV/RtxT7FMv/aGv1Q0fo14sOPqob4PpLWP3o3L0edVTVtOzIXMFtaQsd0XPqm4GLDoIGXTZ5x5ThmglJJPZdoogkp2uAMXty2v1weIXETI5fgHjZoAALQByEw0rHvMHt8FcUJw7LOOJ53mGk/cY0tdLnA82pibVoRhSFuq74AAF/PN7W3HS0NqpFTQpJl6mvSki3aKJJxueub48t8gg1MN3BakD3KGzwZXW8JkAR4vI/VD3+iNdG0hc9O2R+qNPkG3WpRpuYWFuJQEqUOf5+ePIbQ/aKjaoZX7ZJlX+iFbVn0IpPg6j849DhGuD/Y7+TyPzjU7R2O9qkL0EmVK4Qrax/qdhY+q8i5/exDqOEqsgDTJ2B9ZPao3/vRp9oVo72qfZl9Min0JnKeFqsLf/UJ8C6j84Ia4dqYQEqltFtv2qTfn1i/woj2ifzLzcuZ//9k="},
      { id: 4,  name: "Upma",         price: 25, img:"https://media.istockphoto.com/id/1227085744/photo/rava-upma-upma-south-indian-vegetarian-breakfast-with-semolina-and-vegetables.jpg?s=612x612&w=is&k=20&c=j7V8obnudXNIxOsayZFDU2Q2wB5JneTtWBEVMH9G-a8="},
      { id: 5,  name: "Vada Pav",     price: 15, img:"https://media.istockphoto.com/id/1329213718/photo/vada-pav.jpg?s=612x612&w=is&k=20&c=GCBJ6N0dZsK9KeccUpuS8mXabs7lA1uib9Ls9PeOQWQ="},
      { id: 6,  name: "Pattice",      price: 15, img:"https://media.istockphoto.com/id/1329213718/photo/vada-pav.jpg?s=612x612&w=is&k=20&c=GCBJ6N0dZsK9KeccUpuS8mXabs7lA1uib9Ls9PeOQWQ="},
      { id: 7,  name: "Samosa",       price: 20, img:"https://media.istockphoto.com/id/1329213718/photo/vada-pav.jpg?s=612x612&w=is&k=20&c=GCBJ6N0dZsK9KeccUpuS8mXabs7lA1uib9Ls9PeOQWQ="},

    ];
    const menus = [

      { id: 8,  name: "Chole Bhature",price: 60, img:"https://media.istockphoto.com/id/1329213718/photo/vada-pav.jpg?s=612x612&w=is&k=20&c=GCBJ6N0dZsK9KeccUpuS8mXabs7lA1uib9Ls9PeOQWQ="},
      { id: 9,  name: "Coffee",       price: 25, img:"https://media.istockphoto.com/id/1329213718/photo/vada-pav.jpg?s=612x612&w=is&k=20&c=GCBJ6N0dZsK9KeccUpuS8mXabs7lA1uib9Ls9PeOQWQ="},
      { id: 10, name: "Tea",          price: 10, img:"https://media.istockphoto.com/id/1329213718/photo/vada-pav.jpg?s=612x612&w=is&k=20&c=GCBJ6N0dZsK9KeccUpuS8mXabs7lA1uib9Ls9PeOQWQ="},
      { id: 11, name: "Cold Coffee",  price: 30, img:"https://media.istockphoto.com/id/1329213718/photo/vada-pav.jpg?s=612x612&w=is&k=20&c=GCBJ6N0dZsK9KeccUpuS8mXabs7lA1uib9Ls9PeOQWQ="},
      { id: 12, name: "Maggi",        price: 30, img:"https://media.istockphoto.com/id/1329213718/photo/vada-pav.jpg?s=612x612&w=is&k=20&c=GCBJ6N0dZsK9KeccUpuS8mXabs7lA1uib9Ls9PeOQWQ="},
      { id: 13, name: "Sandwich",     price: 40, img:"https://media.istockphoto.com/id/1329213718/photo/vada-pav.jpg?s=612x612&w=is&k=20&c=GCBJ6N0dZsK9KeccUpuS8mXabs7lA1uib9Ls9PeOQWQ="},
      { id: 14, name: "Burger",     price: 50, img:"https://media.istockphoto.com/id/1329213718/photo/vada-pav.jpg?s=612x612&w=is&k=20&c=GCBJ6N0dZsK9KeccUpuS8mXabs7lA1uib9Ls9PeOQWQ="},
    ];

    return (
        <div class="orderBody">
            <div className={styles.orderDetails}>
                <h1 className={styles.odetails}> Order Details </h1>
            </div>
            <div className={styles.cartView}>
                {   menu.filter(e =>  inCart(e.name)).
                    map(e => {e.oprice = e.price; e.price = getVal(e.name) * e.price; return e }).
                    map(e => <FoodCard currentCount={getVal(e.name)} update={true} handler={cardHandler} m={e}/>) }
                    {   menus.filter(e =>  inCart(e.name)).
                      map(e => {e.oprice = e.price; e.price = getVal(e.name) * e.price; return e }).
                      map(e => <FoodCard currentCount={getVal(e.name)} update={true} handler={cardHandler} m={e}/>) }
            <div class="bottom">
                <DatePicker inputClass={styles.clock} _handler={_handler} _count={_count} reqHandler={reqHandler}/>
                <button className={styles.done} onClick={doneFunc}>Done</button>
            </div>
            </div>
        </div>
    );
}

export default Checkout;
