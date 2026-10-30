# Dark tech v2 — phong cách đã duyệt

Áp dụng cho bước hoàn thiện hoặc sửa bản đã duyệt. Đây là hướng dẫn tái tạo phong cách; không copy nội dung/nguồn/timing của video mẫu sang job mới. [Preset JSON](../assets/dark-tech-v2/preset.json) lưu thông số khởi điểm, được điều chỉnh theo footage và yêu cầu mới.

## Nhịp hình và bố cục

Canvas tham chiếu 1080×1920, 30fps. Màu ink #060b13, cyan #66ecf7, violet #b497ff, amber #ffca7b. Chữ đậm dễ đọc, glow mỏng, bo góc; tránh đường viền/trang trí/tag chiếm chỗ nội dung.

**Hai kiểu xen kẽ**, không chia khung hết video:

- Popup: người nói toàn hình, blur khoảng 18px và dim tới brightness≈0.53 chỉ trong insert. Popup phía trước tự cao theo nội dung, thu gọn vào vùng overlay bên dưới. Giữ caption rõ bên dưới. Popup có thể bật từ giữa rồi ổn định phía trên vùng caption; không ép tâm hình học nếu che chữ hoặc khuôn mặt cần thấy.
- Split: thông tin gọn ở trên; người nói **full ngang**, panel bắt đầu khoảng y=920, cao≈1000, crop center và kiểm đủ tóc. Không dùng khung chân dung nhỏ lọt giữa khoảng trống. Không đặt panel xuống y≈1360 khiến tóc bị cắt hoặc mặt nằm quá thấp. **Caption hiện ở giữa màn hình (x≈540/y≈960) khi split**, trở lại trước ngực sau ra. Chỉ hiện source/date/chú thích khi capture có sẵn.

Chọn kiểu theo đoạn/nhịp hoặc xáo trộn có seed, ghi kết quả vào dữ liệu. Không random mỗi render/frame. Các section liên tiếp của cùng bài có thể giữ chung layout để tránh nhấp nháy. Cho cả hai kiểu xuất hiện rõ trong preview.

Chuyển khung người nói bằng geometry/object-position của cùng một video element, ease khoảng 0.55s vào/0.45s ra. Giữ khuôn mặt nguyên hình, không scaleY méo video. Kiểm tóc ở nhiều tư thế, không chỉ một still.

## Popup vừa nội dung, chuyển động đa dạng

Không dùng card cố định 1000px cho mọi nội dung. Header khoảng 72px; footer khoảng 70px khi có một dòng metadata hoặc 108px khi có thêm chi tiết. **Không có chú thích/nguồn/ngày thì không tạo footer**, không chừa hàng trống. Tính chiều cao từ nội dung thực. Loại nhãn “CAPTURE/WEB MOBILE” và số thứ tự trang trí nếu không giúp người xem. Giữ nguồn/ngày/chú thích vốn có; không tự bổ sung khi capture không có, không thêm nhãn giải thích rằng dữ liệu đang thiếu.

Thông số overlay đã duyệt trên canvas 1080×1920: card rộng gốc 952px, tâm x=516, top=280, scale=0.86 cho cả popup và split; left trước scale=40, transform-origin='50% 0%'. Sau scale card rộng khoảng 819px, x≈107…925. Content scale đồng đều=0.68 khi split, =1 khi popup; chiều cao card tính lại theo content đã scale. Không bóp riêng chiều dọc. Nội dung nhiều nên chọn excerpt/crop rõ hơn thay vì thu chữ đến mức khó đọc. Header/footer gọn, không lặp đi lặp lại cùng thông tin.

## Safe zone của overlay

Giữ nguyên bố cục chia hai và A-roll đã duyệt: panel người nói y≈920, caption split x≈540/y≈960, bình thường y≈1290. Khi yêu cầu đưa popup/animation vào safe zone, **chỉ chỉnh các lớp overlay**, không kéo cả composition xuống, không đổi crop người nói hoặc dời phụ đề theo card.

Vùng tham chiếu của bản đã duyệt: x=96…936, y=270…1260; tương đương clip-path `inset(270px 144px 660px 96px)`. Đây là biên dựng tham chiếu cho video dọc, không phải chuẩn pixel chung cho mọi giao diện TikTok/Facebook Reels. Điều chỉnh theo placement thực và nội dung, giữ khoảng trống phía phải cho UI.

- Card dùng vị trí/scale ở trên. Khi split, kiểm cả card cao nhất và footer để không chồng caption y≈960; không tận dụng toàn bộ vùng đến y=1260 cho card split.
- Graphic tự vẽ trên stage gốc 1080×1920: scale=0.8, origin='0 0', left=84, top=210. Stage này là lớp con riêng; A-roll, caption và note ngày không nằm trong transform.
- Chân dung: rộng≈290, ảnh cao≈250, top≈280; left≈100 hoặc right≈180. Giữ nguồn/license đọc được và tránh mặt người nói.
- Áp giới hạn vùng cho card, graphic và chân dung suốt entry/hold/exit. Clip là lớp bảo vệ, không dùng để che mất chữ/nguồn: chỉnh kích thước, crop và quỹ đạo trước; kiểm still ở đầu/giữa/cuối chuyển động. Giữ hiệu ứng bật giữa, trượt trái/phải và rise đa dạng, mượt.

Thông số là điểm khởi đầu tái sử dụng, không ghi đè bố cục khác người dùng đã duyệt. Note ngày và phụ đề giữ thiết kế riêng trừ khi được yêu cầu chỉnh chúng.

## Nhịp animation

Highlight lời nói dùng [ANTON sau đầu](highlight-anton.md): chữ HOA tô đặc, dáng rộng, mỗi đoạn một màu chọn theo nền và lưu cố định, gradient 1/3 phía trên, dim nhẹ và mặt cân sáng. Quy tắc này thay kiểu highlight cũ có viền rỗng/hai màu hoặc card đen; màu cyan/violet/amber phía trên vẫn là tham chiếu cho graphic/evidence, không ép lên highlight.

Các kiểu vào được duyệt: center-pop, trượt trái, trượt phải, trượt xuống từ phía trên. Spring khởi điểm damping=25, stiffness=165, mass=0.85; exit≈0.35s. Drive bằng frame/interpolate/spring, không CSS animation hoặc Math.random theo frame. Fade nhẹ, không rung liên tục.

Cho số liệu: đếm/nhảy số lớn, nhấn mức tăng rồi chuyển sang diện tích/so sánh. **Không cần lưới 100 ô.** Khi chỉ hiện một con số, card co lại; khi xuất hiện nhiều dòng typography thì mở rộng mượt. Ví dụ nhịp: tỷ lệ → mức tăng → diện tích → so sánh ngắn. Phải dùng số thật của lời nói hiện tại, không hardcode dữ kiện của clip mẫu. Với “2–3 tỉnh Việt Nam sau sáp nhập”, chỉ dùng typography khi đó là nội dung người nói; không tự chọn tỉnh hoặc vẽ biên giới như đã có nguồn.

## Tư liệu/ảnh nhân vật

- Capture bài báo thật trên viewport điện thoại; lưu ảnh nguyên gốc và crop render. PNG thực có thể hẹp hơn viewport CSS: dùng đúng chiều rộng ảnh, không hardcode 390px cho mọi ảnh.
- Chọn crop riêng tiêu đề, ảnh và đoạn liên quan. Mỗi view có khoảng 4s đọc rõ sau animation vào; đoạn thoại dài giữ lâu hơn hoặc dùng thêm section/bài cùng ý. Không lướt cả trang nhanh không đọc được.
- Metadata trên hình là tùy chọn theo capture: có nguồn/tác giả/ngày/chú thích thì giữ rõ, không có thì bỏ qua, không điền từ suy đoán hoặc tự thêm từ ghi chú nghiên cứu. Ngày file không là ngày sự kiện; để nội bộ nếu chỉ biết metadata file. Bản đồ mới nhất được đối chiếu theo ngày dữ liệu trong hồ sơ nghiên cứu, không tự in ngày truy cập thành ngày chiến tuyến.
- Nhân vật: chân dung thật thỉnh thoảng bật lên theo tên/ngữ cảnh, có nguồn/năm/license và ghi crop nếu license cần. Có thể đặt góc trên tránh mặt; không gán câu nói của người dẫn thành phát biểu của nhân vật.
- Clip phân tích chính trị có nhận định riêng; graphic chỉ cần mô tả lời nói, không ép mỗi ý kiến phải có bài báo xác nhận. Khi nghiên cứu thấy mâu thuẫn, ghi manifest nội bộ. **Mọi popup không tự thêm** “chưa xác minh”, “chưa xác thực”, “minh họa lập luận”, “không phải thỏa thuận đã chứng minh” hoặc caveat tương tự. Trên hình dùng nội dung nguồn trung thực, không giả screenshot dịch/nguồn/trích dẫn và không âm thầm đổi voice.

## Phụ đề và ngày edit

Phụ đề khởi điểm: ClipSans từ font tiếng Việt hợp lệ (bản được duyệt dùng Segoe UI), 54px/700, line-height 1.23, tối đa hai dòng, khoảng 10–12 từ/thẻ. Width≈900, x=50%, tâm y=1290, translate(-50%,-50%), chữ trắng, stroke đen≈2.8px, bóng mỏng. Ngắt theo nghĩa, đo dòng thực, không cố đủ từ khi làm câu khó hiểu. Caption độc lập với grade/blur/card.

Khi split, giữ caption hiện và nội suy centerY = 1290 − 330 × layoutProgress để đến y=960; khi về A-roll/popup, chuyển mượt về y=1290. Không đổi transcript/timing hoặc cỡ chữ khi đổi vị trí. Người dùng có thể đổi quy tắc này ở job sau.

Ngày edit thật của job, dd/mm/yyyy, khoảng 10s đầu; trái x≈48, y≈58% chiều cao, translateY(-50%). Font36/600, letterSpacing≈1.5, chữ đen, nền rgba(255,255,255,0.5), padding13×20, radius18. Fade/slide nhẹ. Không dùng ngày clip mẫu làm mặc định; giữ ngày đang có nếu người dùng không yêu cầu đổi.

## A-roll sáng trong, hơi lạnh

Chỉ grade lớp A-roll, không grade evidence, chân dung hoặc chữ. Bản đã duyệt dùng SVG feColorMatrix trong sRGB với gain R=0.985, G=1.005, B=1.045, alpha giữ nguyên; sau đó CSS brightness(1.13) contrast(1.025) saturate(1.09). Đây là điểm khởi đầu cho footage tương tự, **không** phải LUT cố định cho mọi camera. Giảm sắc vàng/da cam nhẹ, giữ da tự nhiên, tránh cyan da hoặc đèn trắng cháy.

```tsx
<svg width={0} height={0} style={{position:'absolute',pointerEvents:'none'}} aria-hidden>
  <defs><filter id="aroll-cool-clear" colorInterpolationFilters="sRGB">
    <feColorMatrix type="matrix" values="0.985 0 0 0 0  0 1.005 0 0 0  0 0 1.045 0 0  0 0 0 1 0"/>
  </filter></defs>
</svg>
// Apply only to A-roll video:
// filter: 'url(#aroll-cool-clear) brightness(1.13) contrast(1.025) saturate(1.09)'
```

Popup blur/dim là lớp layout bên ngoài grade. Ở split giữ A-roll rõ; màu video tiếp tục nhất quán. So still bình thường và split; kiểm highlight, màu da và độ bão hòa theo source.

## QA và giao

Kiểm ít nhất đại diện popup, split, card ngắn/dài và các điểm đổi layout. Đủ tóc, không méo mặt, trên không chiếm quá khung; metadata có sẵn đọc được, trường thiếu ẩn; không tự thêm disclaimer hoặc vùng rỗng; caption đúng trạng thái. Kiểm một voice track, proxy không phát tiếng, B-roll muted. Chạy TypeScript và render still để xác nhận; thử playback thật cho lỗi sync/lặp âm. Giữ preview để người dùng review, không tự render toàn MP4. Khi được xuất, dựng hình HD từ source gốc theo cut map rồi áp cùng grade/layout; không phóng proxy thấp.
