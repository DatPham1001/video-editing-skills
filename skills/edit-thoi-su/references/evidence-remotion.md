# Preset evidence-remotion-v1

Quy tắc người dùng hiện hành ưu tiên: capture thiếu chú thích/ngày/nguồn thì bỏ trường đó, ẩn hàng/footer trống; không tự thêm giải thích “chưa xác minh/chưa xác thực” hoặc caveat vào popup. Ghi chú nghiên cứu ở hồ sơ job. Áp cả khi tái dùng preset cũ.

Preset cũ tùy chọn, chỉ dùng khi người dùng yêu cầu tái hiện đúng v1. Mặc định hiện tại là [dark-tech-v2](dark-tech-v2.md): Remotion trực tiếp, tối thiểu khoảng 4s đọc rõ/bài, phụ đề 10–12 từ và xen kẽ popup/split. Không áp mặc định 48px/8 từ, thẻ cố định hoặc thao tác ChatCut của tài liệu này cho job v2.

Áp dụng ở bước2 sau khi bản cắt thô đã được duyệt và người dùng yêu cầu làm tiếp, hoặc khi người dùng yêu cầu bổ sung evidence trên bản dựng hiện tại. Không yêu cầu draft transcript/draft hiệu ứng hay một vòng duyệt kế hoạch hình ảnh riêng. Bổ sung evidence trên bản đã dựng là quyền thực hiện phần bổ sung đó, không cần xin lại cùng quyền.

## Tái sử dụng đúng hiệu ứng

Dùng [component](../assets/evidence-remotion-v1/EvidenceCardV1.tsx) cùng [preset cố định](../assets/evidence-remotion-v1/preset.json). Copy component vào source Remotion và hai font trong `assets/evidence-remotion-v1/fonts/` vào `public/fonts/`. Giữ bản component đã kiểm tra; không viết lại theo trí nhớ hoặc tự đổi palette, vị trí, spring, dimmer, blur và timing. Font là Arial đã dùng trong video tham chiếu; dùng trong cùng môi trường được cấp phép, không tự phát hành font như một sản phẩm riêng.

Preset 1080×1920, 30fps: thẻ trắng 840×960 tại (120,190), bo 22px; kicker teal ở (110,100), nguồn ở (120,1162). Nền dim rgba(5,12,22,.46). Entry: opacity .15→1 trong 5f; spring damping19/stiffness210/mass.65, Y64→0, scale .94→1; xoay -2°→0° trong 12f. Gạch vàng quét từ f7→17. Exit 6f cuối. Chi tiết đầy đủ nằm trong preset JSON và component.

Các effect đã dùng trước đó cũng được giữ nguyên mã nguồn: [StoryCard](../assets/evidence-remotion-v1/StoryCard.tsx) cho thẻ ảnh báo nguyên trang AP/Reuters, câu hỏi, ảnh minh họa, lựa chọn nhà hàng/cà phê và bữa ăn; [Headline](../assets/evidence-remotion-v1/Headline.tsx) cho hook, tiêu đề nhấn và caveat. StoryCard/Headline dùng Props như trong file, cùng font ReferenceSans. Headline có canvas1080×340, cần đặt vị trí theo vùng mặt/caption thực tế; StoryCard dùng1080×1920. Không copy nội dung bài báo hoặc tên file cũ sang job mới. Hai nhánh `ap`/`reuters` của StoryCard giữ crop mẫu1920×1080 cũ; chỉ dùng nguyên crop khi screenshot trùng bố cục, còn bài khác dùng EvidenceCardV1 với regions được kiểm tra.

Chỉ thay nội dung `kicker`, `publisher`, `source`, `regions`, `summary`, `note`, `summaryTop` và thời lượng. Đăng ký từng Composition riêng với defaultProps inline, fps30, width1080, height1920. Thời lượng nên 3–5s, canh câu nói thật; nếu câu ngắn có thể khoảng 2.9s. Không kéo thẻ sang luận điểm chưa có nguồn chỉ để đủ thời lượng.

`regions` là các cửa sổ crop trên screenshot gốc: image đường dẫn tương đối trong public, imageWidth/imageHeight đúng pixel gốc, crop x/y/width/height theo ảnh gốc, left/top/width theo hệ tọa độ trong thẻ. Component tính một tỉ lệ duy nhất để không méo ảnh. Giữ tiêu đề, ngày và tên nguồn đọc được; loại menu, quảng cáo, cookie banner và bài liên quan. Chụp trang thật, không tái tạo masthead hay bịa trích dẫn. Có thể dùng thêm vùng ảnh thực sự thuộc bài đó. Phần tiếng Việt đặt dưới nhãn “TÓM TẮT BIÊN TẬP” là diễn giải của biên tập, không phải trích nguyên văn báo.

Ảnh crop kết thúc trước summaryTop-42; summary tối đa 2 dòng, font54, tránh ngắt dòng tự phát sinh dòng thứ ba. Note tối đa2 dòng. Bảo đảm `summaryTop+182+2*34*1.25 <=960` nếu dùng note2 dòng, hoặc không ghi note khi phần ảnh chiếm nhiều chỗ. Nguồn và thẻ phải ở phía trên phụ đề; bản tham chiếu dùng caption48px, trước ngực, top1414. Bản dựng khác phải kiểm tra mặt/caption thực tế.

## Nguồn và câu neo

Đọc nội dung hỗ trợ, đối chiếu sự kiện/ngày/địa điểm với câu nói. Ghi URL, tiêu đề, tác giả, ngày xuất bản/cập nhật, ngày truy cập, ý được hỗ trợ và giới hạn trong manifest của job. Dùng supports/partial/unverified; một bài báo không chứng minh mọi ý trong cùng câu. Không lấy GDP làm lương, lời kêu gọi tương lai làm sự kiện đã xảy ra, đề xuất cải cách làm luật đã thi hành, một vụ án làm thống kê cả xã hội. Giữ cờ review cho phần chưa được chứng minh. Không thay lời hoặc cắt luận điểm mới nếu chưa có quyền.

Ưu tiên screenshot có sẵn trong evidence nếu đúng bài. Nếu thiếu, tìm nguồn trực tiếp, chụp phần cần dùng; không dùng trang đăng nhập/paywall thay nội dung. Không dán toàn bộ bài báo vào template/skill. Tin đăng lại cùng Reuters/AP là cùng một nguồn, không phải xác nhận độc lập. Skill chỉ lưu phong cách và code; các bài báo, media, asset/item/project ID nằm trong job hiện tại.

## Render và chèn ChatCut

Mở Studio của project đang có trước khi sửa và giữ tab. Render asset để chèn theo yêu cầu dựng của người dùng:

```powershell
node node_modules/@remotion/cli/remotion-cli.js still src/index.ts Evidence output/Evidence-proof.png --frame=35
node node_modules/@remotion/cli/remotion-cli.js render src/index.ts Evidence output/Evidence.webm --codec=vp9 --image-format=png --pixel-format=yuva420p --video-bitrate=5M --concurrency=2
```

Nếu node không trong PATH, dùng đường dẫn runtime được công cụ cung cấp. Giữ alpha, không xuất nền đen MP4. WebM không có audio. Kiểm tra still và alpha trước import. Import qua plugin asset-import, một batch với assetId ổn định; lưu manifest job. Đặt video overlay trên track phía trên A-roll đúng frame đã đọc từ timeline mới nhất, khung1080×1920, fit contain, sourceStart=0. Không ripple và không dựng phẳng cả video.

**Gaussian Blur radius180 phải gắn vào từng clip A-roll đang nằm dưới thẻ**, không gắn vào video thẻ báo hay caption. Với mỗi clip, phạm vi effect là giao của clip và thẻ, tọa độ fromFrame tuyệt đối theo timeline. Hiện tại gọi effect theo range của track có thể chỉ gắn clip đầu: luôn lập từng targetItemId.

Dùng [planner](../scripts/plan_evidence_insert.py) với clips vừa đọc từ ChatCut; input là mảng `{id,fromFrame,endFrame}` hoặc `{id,fromFrame,durationInFrames}`. Planner từ chối gap/overlap và chỉ ghi JSON adds, chưa sửa project:

```powershell
python plan_evidence_insert.py --clips current-clips.json --asset-id ASSET_ID_FROM_IMPORT --from-frame 100 --duration 120 --overlay-track V2 --output adds.json
```

Thay các giá trị ví dụ bằng asset/track/range thật. Kiểm tra overlay không trùng item cùng track; gọi edit_item validateOnly trước commit. Project và timeline ID lấy từ read_project; không lưu vào preset.

## Kiểm tra và lưu

Đọc lại cấu trúc sau commit; phải đủ overlay và blur trên tất cả clip giao nhau. Xem composed frames ở trước vào, entry, giữa, cuối, sau ra và quanh các mối cắt A-roll để xác nhận blur không nhấp nháy. Kiểm tra source/ngày không bị crop, caption không đè thẻ, alpha và đuôi fade sạch. Không coi render thành công là đã xem được timeline.

Không gọi global caption resegmentation khi chỉ thêm evidence: có thể làm mất custom text/name flags. Giữ revision và nội dung captions hiện có, xác nhận không đổi. Nếu UI báo stale nhưng source không đổi, chỉ kiểm tra trạng thái; không tự repaginate.

Lưu manifest job gồm props/crop, source, source-claim mapping, timeline in/out, asset/item/effect IDs thực tế, component/preset/font SHA256 và ảnh kiểm tra. Skill chứa component/preset/font đã kiểm thử; muốn đổi phong cách thì tạo v2, giữ nguyên v1 để tái dùng y hệt.
