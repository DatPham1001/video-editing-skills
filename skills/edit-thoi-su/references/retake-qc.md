# Rà nói lặp và nói lại sau dựng

Dùng khi cắt thô bước1, chốt A-roll, hoặc người dùng báo còn nói lặp trên bản dựng. Phân biệt lần nói lại hỏng/đã được bao trùm với lặp có chủ ý để nhấn, câu chuyển ý, phép đối và lời kết. Giữ một lần nói hoàn chỉnh, đủ chủ ngữ và ý; bỏ trọn lần khởi động lại bị thừa. Không ghép các mảnh dở của nhiều take thành một câu giả. Transcript là công cụ nội bộ, không phải sản phẩm draft cần duyệt trước cắt.

## Đọc chữ chưa đủ

ASR có thể gộp nhiều lần nói cùng cụm thành một dòng, bỏ hẳn câu lặp, hoặc gán cả một cụm nói lại vào token ngắn như “và”, “các”. Khi token một từ kéo dài bất thường hoặc người dùng báo lặp dù transcript chỉ xuất hiện một lần, không kết luận video không lặp. Kiểm tra audio tương ứng trong source và bản dựng, đối chiếu source in/out của từng clip. Một segment/clip không đồng nghĩa một câu hoặc một take.

Kiểm tra có ngữ cảnh trước và sau đoạn nghi vấn. Nếu không có khả năng nghe trực tiếp, có thể dùng nhận dạng độc lập trên audio để đối chiếu, kiểm từng lần khởi động lại và mốc source; ghi đúng phương pháp và giới hạn, không nói đã nghe/xem toàn bộ chỉ từ ASR hay vài frame. Không đổi transcript nguồn sang bản ASR mới hàng loạt, vì sẽ làm hỏng các caption đã sửa.

## Quyết định cắt

Ghi cho mỗi cụm: câu chủ đích, các lần thử, phạm vi source và timeline thật, lần giữ, lần bỏ và lý do. Đánh dấu toàn bộ take thừa, kể cả đầu câu cùng nghĩa và đuôi từ nối bị bỏ dở; đừng chỉ xóa một từ lặp trên phụ đề mà âm thanh vẫn phát hai lần. Giữ phần setup chưa được lặp ở take tốt. Chỉ cắt khi xác định được nội dung và ranh giới; không dùng khoảng lặng/thiếu ASR để đoán từ không tồn tại.

Áp dụng quy tắc cắt khoảng không nói đã được người dùng chỉ định trong SKILL.md, nhưng tách quyết định đó khỏi quyết định cắt retake. Không chạy bulk silence cleanup khi yêu cầu chỉ sửa nói lặp trên bản đã dựng.

Trong ChatCut dùng Script mới: read_script → sửa timelineMd/timeline.md → apply_script preview → commit khi preview đúng phần đã được yêu cầu. Không dùng split/delete item làm đường tắt chọn lời nói. Giữ nguyên metadata và occurrence của các hàng hiện tại; không sửa câu ASR thành câu mới trong Script. Nếu một hàng đại diện cả take bị lặp, bỏ cả hàng đó khi đã xác nhận audio, kể cả khi chữ trên hàng rất ngắn.

## Bản dựng đã có phụ đề/evidence/hiệu ứng

Trước cắt lưu snapshot mới của clip source mapping, gain/fade, caption text/timing/layout, overlay với source offset, attached effects và markers. Dùng trạng thái hiện tại, không đè bằng manifest cũ nếu người dùng đã sửa. Preview phải cho biết phần bị bỏ và tổng độ dài giảm; nếu thay đổi ngoài phạm vi dự kiến, sửa kế hoạch trước commit.

Sau cắt tính lại timing theo các khoảng đã xóa. Dời các overlay/marker phía sau; với overlay giao đoạn xóa, quyết định cắt ngắn, đặt lại vào câu neo, render lại hoặc bỏ khi không còn câu neo. Không chỉ ripple A-roll rồi để evidence/highlight đứng ở thời gian cũ. Giữ sourceStart của clip đồ họa, nhất là các scene được đóng gói chung trong library.

Với clip đã bị cắt sát theo VAD, Script có thể snap lại đầu/đuôi từ ngoài đúng các hàng bị xóa. So sánh preview với native mapping và khi cần cả preview không sửa để phân biệt reflow với phần cắt retake; không chấp nhận drift ngoài phạm vi một cách mù quáng. Lưu backup timeline trước khi commit. Nếu cleanup được phép bao gồm sửa ranh giới từ và phải reflow, kiểm lại audio rồi map overlay/marker qua source time sang timeline mới; một offset tổng không đủ. Với video đồ họa đã bake, giữ trọn source range animation bằng rate mới hoặc render lại khi duration đổi, không cắt mất animation ra.

Kiểm tra lại gain và fades được giữ; smooth_audio theo độ dài crossfade đã dùng để nối các mối cắt sau reflow. Đọc lại Gaussian Blur trên từng clip nền vì ID/range có thể thay đổi; không blur chữ hay caption. Sau đó đối chiếu phụ đề với audio và bản backup: bỏ chữ của take đã xóa, giữ các sửa chính tả/tên riêng, giới hạn 2 dòng/10–12 từ và vị trí trước ngực. Chỉ sửa các thẻ chịu ảnh hưởng; không repaginate/reset toàn bộ để giải quyết lỗi cục bộ.

## Điều kiện bàn giao

Đọc lại Script và kiểm đoạn trước–mối cắt–đoạn sau; xác nhận chỉ còn một phiên bản đầy đủ của câu. Rà toàn bộ bản dựng cho cụm mở đầu bị nói lại, false start và lặp ý không bổ sung thông tin. Kiểm tiếp các mối cắt mới, caption, evidence và highlight quanh phần dời thời gian. Lưu log đã kiểm tới đâu, bằng audio/ASR/cấu trúc/frame nào; không báo QC toàn clip nếu chưa kiểm đủ. Nói rõ phần đã bỏ và thời lượng mới bằng lời nói/timecode, không đưa sN/cN cho người dùng.

